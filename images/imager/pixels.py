"""
An abstraction class for OpenGL image buffers

For simplicity, we would like to treat an image as a (1D) list of tuples. In 
reality, it is a little more complicated than that, because OpenGL expects the 
data in a very compact format. This data structure abstracts all of this so we 
can pretend otherwise.

You DO NOT need to understand this file. This is an extremely advanced Python 
class. You only need to use it (and even then, since it is a subclass of list),
you may not be aware that you are using it.

Author: Walker M. White (wmw2)
Date:   October 26, 2025
"""
from array import array             # Byte buffers
from io import StringIO             # Making complex strings
from itertools import islice


# Performance generators
def flatten_pixels(data):
    """
    Generates the individual pixels from a pixel list.
    
    This generator is used to flatten out a pixel list for internal processing.
    If the list is already flattened, this generator just enumerates the elements
    of the list
    
    Parameter data: The data to flatten
    Precondition: data is an iterable of ints or of pixels (3-element tuples)
    """
    for p in data:
        try:
            if type (p) in (tuple, list):
                yield int(p[0]) & 0xFF
                yield int(p[1]) & 0xFF
                yield int(p[2]) & 0xFF
            else:
                yield int(p) & 0xFF
        except:
            raise ValueError(f'pixel {repr(p)} is corrupted') from None


def concatenate(data1,data2):
    """
    Generates the concatenation of two iterables
    
    This can be used to glue two generators together. We make no assumption of
    the generator contents.
    
    Parameter data1: The initial data segment
    Precondition: data1 is an iterable
    
    Parameter data2: The terminal data segment
    Precondition: data2 is an iterable
    """
    for x in data1:
        yield x
    for y in data2:
        yield y


# The class abstraction
class Pixels(list):
    """
    A class to convert an image into a list of tuples
    
    The objects of the class are not lists. But they behave exactly like lists 
    in any way that matters. It has no public attributes other than the buffer 
    property, which allows direct access to the underlying byte buffer.
    
    The primary initialization of this class creates an empty pixel list (of the 
    requested size). This class also has the ability to initialize its data 
    from a list via alternate classmethod constructors.
    
    These pixels in this list are not RGB objects, like in Assignment 3.  They 
    are tuples, which are lists that cannot be modified (so you can slice them 
    to get new tuples, but not assign or append to them).
    
    The methods progress() and unmark() are used to track changes to this pixel 
    list. These methods are used by the progress bar to display how much of the 
    image has been modified.
    """
    # Freeze the attributes
    __slots__ = ("_buffer","_width","_marker","_change")
    
    @property
    def buffer(self):
        """
        The underlying byte buffer
        """
        return self._buffer

    @property
    def width(self):
        """
        The image width
        """
        return self._width
    
    @width.setter
    def width(self,value):
        assert type(value) == int and value > 1, f'{repr(value)} is an invalid width'
        self._width = value
    
    # INITIALIZER
    def __init__(self,value):
        """
        Initializer: Creates a new pixel list
        
        The given value can be one of three types
        
        1. An integer >= 0
        2. An string representing a file name
        3. An iterable of 3-element pixels
        
        In the case of 1, the pixel list created consists of all 0s. Otherwise,
        the pixel list is initialized with the appropriate data.
        
        Note that the pixel width is 1 unless value has a width attribute.
        
        Parameter value: the initialization value
        Precondition: value is one of the three types above
        """
        if type(value) == int:
            assert value >= 0, repr(size)+' is negative'
            
            self._buffer = array('B',(0 for _ in range(value*3)))
            self._width = 1
        elif type(value) == str:
            from PIL import Image as CoreImage
            
            try:
                image  = CoreImage.open(value)
                image  = image.convert("RGB")
                self._buffer = array('B',flatten_pixels(image.getdata()))
                self._width = image.size[0]
            except:
                raise FileNotFoundError(f'Could not load the image file {repr(value)}.') from None
        else:
            try:
                self._buffer = array('B',flatten_pixels(value))
            except:
                raise ValueError('Attempt to initialize with unsupported pixel data') from None
        
            elts = len(self._buffer)
            assert elts % 3 == 0, 'attempt to initialize with corrupted pixel data'
            
            if hasattr(value,'width'):
                self._width = value.width
            else:
                self._width = 1
        
        self.unmark()
    
    # DISPLAY METHODS
    def __str__(self):
        """
        Returns: this pixel list as a string. 
        
        The value shown will look identical to a list of tuples.
        """
        output = StringIO()
        output.write('[')
        after = False
        for pixel in self:
            if after:
                output.write(', ')
            output.write(str(pixel))
            after = True
        output.write(']')
        
        result = output.getvalue()
        output.close()
            
        return result
    
    def __repr__(self):
        """
        Returns: the unambiguous representation of this pixel list
        
        The value shown will make it clear this is a Pixels object and not an 
        actual list.
        """
        return 'Pixels'+str(self)
    
    # LIST IMPERSONATION METHODS
    def __len__(self):
        """
        Returns: The length of this pixel list.
        
        This method defines the return value of the len() function.
        """
        return len(self._buffer)//3
    
    def __getitem__(self, idx):
        """
        Returns: The element or sublist indentified by index.
        
        This method allows for either single element access (p[0]) or a slice
        (p[1:3]).  This method is used for getting elements, not setting them.
        
        Parameter idx: The pixel list index
        Precondition: idx is either an int or a slice
        """
        if isinstance(idx, slice):
            start, stop, step = idx.indices(len(self))
            it = (self._triplet_at(i) for i in range(start, stop, step))
            return self.__class__(it)
        # int index
        if idx < 0:
            idx += len(self)
        if not (0 <= idx < len(self)):
            raise IndexError("index out of range")
        return self._triplet_at(idx)
    
    def __setitem__(self, idx, value):
        """
        Sets the element or sublist indentified by index to be the new value
        
        This method allows for either single element access (p[0] = (255,0,255)) 
        or a slice (p[1:3] = [(255,0,255),(0,0,0)]). This method is used for 
        setting elements, not getting them.
        
        Parameter idx: The pixel list index
        Precondition: idx is either an int or a slice
        
        Parameter value: The new value for the position or slice
        Precondition: index must be a tuple or a list of tuples
        """
        if isinstance(idx, slice):
            start, stop, step = idx.indices(len(self))
            if step != 1:
                # Must be length-preserving for extended slices
                values = list(value)
                if len(values) != len(range(start, stop, step)):
                    raise ValueError("attempt to assign sequence of size "
                                     f"{len(values)} to extended slice of size "
                                     f"{len(range(start, stop, step))}")
                for i, v in zip(range(start, stop, step), values):
                    self._set_triplet_at(i, v)
            else:
                # Replace a contiguous block
                new_bytes = array('B')
                for t in value:
                    new_bytes.extend(self._norm_triplet(t))
                a = 3 * start
                b = 3 * stop
                self._buffer[a:b] = new_bytes
                
                prev = 0
                for pos in range(index.start,index.stop):
                    if self._marker[pos]:
                        prev += 1
                self._marker[index.start:index.stop] = [1]*len(value)
                self._change += len(value)-prev
        else:
            self._set_triplet_at(idx, value)
    
    def __iter__(self):
        """
        Returns: An iterator for the pixel list
        
        This allows the pixel list to be used in for-loops
        """
        return _PixelIterator(self)
    
    # CORE HELPERS
    @staticmethod
    def _norm_triplet(t):
        """
        Returns a tuple that normalizes the pixel to within range
        
        Parameter t: The input tuple
        Precondition: t is a three-element tuple of int compatible values
        """
        try:
            r, g, b = t
            return (int(r) & 0xFF, int(g) & 0xFF, int(b) & 0xFF)
        except:
            raise ValueError(f'pixel data {repr(t)} is corrupted') from None
    
    def _triplet_at(self, i):
        """
        Returns the 3-element tuple at position i
        
        Parameter i: The element position
        Precondition: i is an int 0..size-1
        """
        base = 3 * i
        d = self._buffer
        return (d[base], d[base + 1], d[base + 2])
    
    def _set_triplet_at(self, i, t):
        """
        Sets a triplet value at position i
        
        Parameter t: The input tuple
        Precondition: t is a three-element tuple of int compatible values

        Parameter i: The element position
        Precondition: i is an int 0..size-1
        """
        base = 3 * i
        r, g, b = self._norm_triplet(t)
        
        d = self._buffer
        d[base] = r
        d[base + 1] = g
        d[base + 2] = b
        
        if not self._marker[i]:
            self._marker[i] = 1
            self._change += 1
    
    # MUTATION API
    def append(self, t):
        """ 
        Appends the given list to this pixel
        
        Parameter t: The input tuple
        Precondition: t is a three-element tuple of int compatible values
        """
        self._buffer.extend(self._norm_triplet(t))
        self.unmark()
    
    def extend(self, it):
        """
        Extends this object by the given pixel iterator
        
        Parameter it: The input iterator
        Precondition: it is an iterator of valid pixel values
        """
        self._buffer.extend(flatten_pixels(it))
        self.unmark()
    
    def insert(self, i, t):
        """
        Inserts a pixel at the given position.
        
        All other pixels are shifted right.
        
        Parameter i: The element position
        Precondition: i is an int 0..size-1
        
        Parameter t: The input tuple
        Precondition: t is a three-element tuple of int compatible values
        """
        n = len(self)
        if i < 0:
            i += n
        i = max(0, min(i, n))
        pos = 3 * i
        self._buffer[pos:pos] = array('B', self._norm_triplet(t))
        self.unmark()

    def pop(self, i=-1):
        """
        Pops from the pixel list at the given position
        
        Parameter i: The element position
        Precondition: i is an int 0..size-1
        """
        n = len(self)
        if n == 0:
            raise IndexError("pop from empty list")
        if i < 0:
            i += n
        if not (0 <= i < n):
            raise IndexError("pop index out of range")
        pos = 3 * i
        d = self._buffer
        item = (d[pos], d[pos + 1], d[pos + 2])
        del d[pos:pos + 3]
        self.unmark()
        return item

    def clear(self):
        """
        Erases the contents of this pixel list
        """
        self._data = array('B')
    
    # LIST COMBINATION METHODS
    def copy(self):
        """
        Returns a copy of this pixel list
        """
        return self.__class__(self._buffer)
    
    def __add__(self, other):
        """
        Adds a list to this pixel list, creating a copy
        
        This only succeeds if the contents of the list other are in the right 
        form.
        
        Parameter other: The list to add
        Precondition: other is a Pixel list
        """
        result = self.__class__(concatenate(self._buffer,flatten_pixels(other)))
        result.width = self.width
        return result

    def __iadd__(self, other):
        """
        Adds a list to this pixel list in place
        
        This only succeeds if the contents of the list other are in the right 
        form.
        
        Parameter other: The list to add
        Precondition: other is a Pixel list
        """
        self.extend(other)
        return self
    
    def __mul__(self, n):
        """
        Multiplies this pixel list by the given integer.
        
        Parameter n: The multiplicative factor
        Precondition: n is an integer
        """
        assert type(n), repr(n)+' is not an integer'
        
        result = self.__class__(0)
        result._buffer = self._buffer * max(0,k)
        result.width = self.width
        return result
    
    # PROGRESS MONITOR
    def progress(self):
        """
        Returns: the progress percentage of this image
        
        This value returned is in the range [0,1]. It is the percentage of pixels that
        have been modified since unmark() was last called.
        """
        return self._change/len(self)
    
    def unmark(self):
        """
        Resets the progress monitor to 0.
        
        This clears all change tracking.
        """
        self._marker = [0]*len(self)
        self._change = 0


class _PixelIterator(object):
    """
    A (hidden) class for iterating through pixel lists
    
    This class allows a Pixels object to be used in a for-loop. Note that this
    iterates pixels (3-element tuples), not individual color values.
    """
    
    def __init__(self,pixels):
        """
        Initializer: Creates an iterator for the given pixel list
        
        Paramater pixels: A pixel list
        Precondition: pixels is a Pixels object
        """
        self._pixels = pixels
        self._pos = 0
        self._len = len(pixels)
    
    def __next__(self):
        """
        Returns: The next element in the iteration
        
        This method raises StopIteration when it reaches the end of the
        iteration.  This will cause the for-loop to stop.
        """
        if self._pos >= self._len:
            raise StopIteration
        else:
            self._pos += 1
            return self._pixels[self._pos-1]
