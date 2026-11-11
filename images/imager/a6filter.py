"""
Image processing methods for the imager application.

This module provides all of the image processing operations that are called 
whenever you press a button. Some of these are provided for you and others you
are expected to write on your own.

Note that this class is a subclass of Canvas. This allows you to make use
of the undo functionality. You do not have to do anything special to take 
advantage of this. Just make sure you use getCurrent() to access the most 
recent version of the image.

Based on an original file by Dexter Kozen (dck10) and Walker White (wmw2)

YOUR NAME(S) AND NETID(S) HERE
DATE COMPLETED HERE
"""
import a6canvas


# TASK 3: IMPLEMENT THIS CLASS
class Filter(a6canvas.Canvas):
    """
    A class that contains a collection of image processing methods
    
    This class is a subclass of Canvas. That means it inherits all of the 
    methods and attributes of that class too. We do that (1) to put all of the 
    image processing methods in one easy to read place and (2) because we might 
    want to change how we implement the undo functionality later.
    
    This class is broken into three parts (1) implemented non-hidden methods, 
    (2) non-implemented non-hidden methods and (3) hidden methods. The 
    non-hidden methods each correspond to a button press in the main 
    application.  The hidden methods are all helper functions.
    
    Each one of the non-hidden functions should edit the most recent image 
    in the edit history (which is inherited from Canvas).
    """
    
    # PROVIDED ACTIONS (STUDY THESE)
    def invert(self):
        """
        Inverts the current image, replacing each element with its color complement
        """
        current = self.getCurrent()
        for pos in range(current.getLength()):
            rgb = current.getFlatPixel(pos)
            red   = 255 - rgb[0]
            green = 255 - rgb[1]
            blue  = 255 - rgb[2]
            rgb = (red,green,blue)
            current.setFlatPixel(pos,rgb)
    
    def transpose(self):
        """
        Transposes the current image
        
        Transposing is tricky, as it is hard to remember which values have been 
        changed and which have not.  To simplify the process, we copy the 
        current image and use that as a reference.  So we change the current 
        image with setPixel, but read (with getPixel) from the copy.
        """
        current  = self.getCurrent()
        original = current.copy()
        current.setWidth(current.getHeight())
        
        for row in range(current.getHeight()):      # Loop over the rows
            for col in range(current.getWidth()):   # Loop over the columnns
                current.setPixel(row,col,original.getPixel(col,row))
    
    def reflectHori(self):
        """
        Reflects the current image around the horizontal middle.
        """
        current = self.getCurrent()
        for h in range(current.getWidth()//2):      # Loop over the columnns
            for row in range(current.getHeight()):  # Loop over the rows
                k = current.getWidth()-1-h
                current.swapPixels(row,h,row,k)
    
    def rotateRight(self):
        """
        Rotates the current image left by 90 degrees.
        
        Technically, we can implement this via a transpose followed by a 
        vertical reflection. However, this is slow, so we use the faster 
        strategy below.
        """
        current  = self.getCurrent()
        original = current.copy()
        current.setWidth(current.getHeight())
        
        for row in range(current.getHeight()):      # Loop over the rows
            for col in range(current.getWidth()):   # Loop over the columnns
                pixel = original.getPixel(original.getHeight()-col-1, row)
                current.setPixel(row, col, pixel)
    
    def rotateLeft(self):
        """
        Rotates the current image left by 90 degrees.
        
        Technically, we can implement this via a transpose followed by a 
        vertical reflection. However, this is slow, so we use the faster 
        strategy below.
        """
        current  = self.getCurrent()
        original = current.copy()
        current.setWidth(current.getHeight())
        
        for row in range(current.getHeight()):      # Loop over the rows
            for col in range(current.getWidth()):   # Loop over the columnns
                pixel = original.getPixel(col, original.getWidth()-row-1)
                current.setPixel(row, col, pixel)
    
    # PART A
    def posterize(self):
        """
        Converts the current image to 8-bit color with a posterization effect
        
        Posterization quantizes the pixels, reducing the image from 32-bit
        (also known as 24-bit true color) to 8-bit color. This is done by 
        computing
        
            c = (c // 32) * 32
        
        for red and green, and computing
        
            b = (b // 64) * 64
            
        for blue.
        """
        current = self.getCurrent()
        for pixel in range(current.getLength()):
            rgb = current.getFlatPixel(pixel)
            red = (rgb[0] // 32) * 32
            green = (rgb[1] // 32) * 32
            blue = (rgb[2] // 64) * 64
            current.setFlatPixel(pixel,(red,green,blue))
    
    # PART B
    def reflectVert(self):
        """ 
        Reflects the current image around the vertical middle.
        """
        current = self.getCurrent()
        for col in range(current.getWidth()):          
            for row in range(current.getHeight() // 2): 
                opposite = current.getHeight() - 1 - row
                current.swapPixels(row, col, opposite, col)  
    # PART C
    def jail(self):
        """
        Puts jail bars on the current image
        
        The jail should be built as follows:
        * Put 3-pixel-wide horizontal bars across top and bottom,
        * Put 4-pixel vertical bars down left and right, and
        * Put n 4-pixel vertical bars inside, where n is 
          (number of columns - 8) // 50.
        
        Note that the formula for the number of interior bars is explicitly
        not counting the two bars on the outside.
        
        The n+2 vertical bars should be as evenly spaced as possible.
        """
        current = self.getCurrent()
        width = current.getWidth()
        height = current.getHeight()
        red = (255, 0, 0)

        for row in range(height):
            for col in range(width):
                if row < 3 or row >= height - 3:
                    current.setPixel(row, col, red)

        if width >= 4:
            interior = max(0, (width - 8) // 50)
            spacing = (width - 4) / (interior + 1)
            for bar in range(interior + 2):
                self._drawVBar(round(bar * spacing), red)
    
    # PART D
    def vignette(self):
        """
        Modifies the current image to simulates vignetting (corner darkening).
        
        Vignetting is a characteristic of antique lenses. This plus sepia tone 
        helps give a photo an antique feel.
        
        To vignette, darken each pixel in the image by the factor
        
            1 - (d / hfD)^2
        
        where d is the distance from the pixel to the center of the image and 
        hfD (for half diagonal) is the distance from the center of the image 
        to any of the corners.  The values d and hfD should be left as floats
        and not converted to ints.
        """
        current = self.getCurrent()
        center_x = current.getWidth() / 2
        center_y = current.getHeight() / 2
        half_diagonal_squared = center_x ** 2 + center_y ** 2

        for row in range(current.getHeight()):
            for col in range(current.getWidth()):
                distance_squared = (col - center_x) ** 2 + (row - center_y) ** 2
                factor = 1 - distance_squared / half_diagonal_squared
                pixel = current.getPixel(row, col)
                darkened = (round(pixel[0] * factor),
                            round(pixel[1] * factor),
                            round(pixel[2] * factor))
                current.setPixel(row, col, darkened)
    
    # HELPER METHODS
    def _drawHBar(self, row, pixel):
        """
        Draws a horizontal bar on the current image at the given row.
        
        This method draws a horizontal 3-pixel-wide bar at the given row 
        of the current image. This means that the bar includes the pixels 
        row, row+1, and row+2. The bar uses the color given by the pixel 
        value.
        
        Parameter row: The start of the row to draw the bar
        Precondition: row is an int, 0 <= row  &&  row+2 < image height
        
        Parameter pixel: The pixel color to use
        Precondition: pixel is a 3-element tuple (r,b,g) of ints in 0..255
        """
        current = self.getCurrent()
        for col in range(current.getWidth()):
            current.setPixel(row,   col, pixel)
            current.setPixel(row+1, col, pixel)
            current.setPixel(row+2, col, pixel)
    
    # ADDITONAL HELPER METHODS (ADD WHAT YOU NEED HERE)
    def _drawVBar(self, col, pixel):
        """
        Draws a four-pixel-wide vertical bar on the current image.

        Parameter col: the leftmost column of the bar
        Precondition: col is an int, 0 <= col and col + 3 < image width

        Parameter pixel: the color of the bar
        Precondition: pixel is a 3-element tuple of ints in 0..255
        """
        current = self.getCurrent()
        for row in range(current.getHeight()):
            for offset in range(4):
                current.setPixel(row, col + offset, pixel)

    
