"""
Steganography methods for the imager application.

This module provides all of the test processing operations (encode, decode) 
that are called by the application. Note that this class is a subclass of Filter. 
This allows us to layer this functionality on top of the Instagram-filters, 
providing this functionality in one application.

Based on an original file by Dexter Kozen (dck10) and Walker White (wmw2)

Avi Sharma (as4632)
November 11, 2026
"""
import a6filter


class Encoder(a6filter.Filter):
    """
    A class that contains a collection of image processing methods
    
    This class is a subclass of Filter.  That means it inherits all of the 
    methods and attributes of that class too. We do that separate the 
    steganography methods from the image filter methods, making the code
    easier to read.
    
    Both the `encode` and `decode` methods should work with the most recent
    image in the edit history.
    """
    
    def encode(self, text):
        """
        Returns True if it could hide the text; False otherwise.
        
        This method attemps to hide the given message text in the current 
        image. This method first converts the text to a byte list using the 
        encode() method in string to use UTF-8 representation:
            
            blist = list(text.encode('utf-8'))
        
        This allows the encode method to support all text, including emoji.

        The first four pixels contain the marker 173, 42, 219, 86. The next
        two contain the byte length as two base-1000 digits. Each following
        pixel contains one UTF-8 byte. Thus the encoding uses six extra pixels.
        
        If the text UTF-8 encoding requires more than 999999 bytes or the 
        picture does  not have enough pixels to store these bytes this method
        returns False without storing the message. However, if the number of
        bytes is both less than 1000000 and less than (# pixels - 10), then 
        the encoding should succeed.  So this method uses no more than 10
        pixels to store additional encoding information.
        
        Parameter text: a message to hide
        Precondition: text is a string
        """
        # You may modify anything in the above specification EXCEPT
        # The first line (Returns True...)
        # The last paragraph (If the text UTF-8 encoding...)
        # The precondition (text is a string)
        assert isinstance(text, str)
        data = text.encode('utf-8')
        image = self.getCurrent()
        if len(data) > 999999 or len(data) + 6 > image.getLength():
            return False

        marker = (173, 42, 219, 86)
        header = marker + (len(data) // 1000, len(data) % 1000)
        for pos in range(len(header)):
            self._encode_pixel(pos, header[pos])
        for pos in range(len(data)):
            self._encode_pixel(pos + len(header), data[pos])
        return True
    
    def decode(self):
        """
        Returns the secret message (a string) stored in the current image. 
        
        The message should be decoded as a list of bytes. Assuming that a list
        blist has only bytes (ints in 0.255), you can turn it into a string
        using UTF-8 with the decode method:
            
            text = bytes(blist).decode('utf-8')

        The first four pixels must contain the marker 173, 42, 219, 86.
        The next two give the byte length in base 1000, followed by one
        pixel per byte. Invalid lengths, bytes, or UTF-8 are rejected.
        
        If no message is detected, or if there is an error in decoding the
        message, this method returns None
        """
        # You may modify anything in the above specification EXCEPT
        # The first line (Returns the secret...)
        # The last paragraph (If no message is detected...)
        image = self.getCurrent()
        if image.getLength() < 6:
            return None
        marker = (173, 42, 219, 86)
        if any(self._decode_pixel(pos) != marker[pos] for pos in range(4)):
            return None
        length = self._decode_pixel(4) * 1000 + self._decode_pixel(5)
        if length > 999999 or length > image.getLength() - 6:
            return None
        values = [self._decode_pixel(pos + 6) for pos in range(length)]
        if any(value > 255 for value in values):
            return None
        try:
            return bytes(values).decode('utf-8')
        except UnicodeDecodeError:
            return None
    
    # HELPER METHODS
    def _decode_pixel(self, pos):
        """
        Return: the number n hidden in pixel pos of the current image.
        
        This function assumes that the value was a 3-digit number encoded as 
        the last digit in each color channel (e.g. red, green and blue).
        
        Parameter pos: a pixel position
        Precondition: pos is an int with  0 <= p < image length (as a 1d list)
        """
        # This is helper. You do not have to use it. You are allowed to change it.
        # There are no restrictions on how you can change it.
        rgb = self.getCurrent().getFlatPixel(pos)
        red   = rgb[0]
        green = rgb[1]
        blue  = rgb[2]
        return  (red % 10) * 100  +  (green % 10) * 10  +  blue % 10
    
    # ADDITONAL HELPER METHODS (ADD WHAT YOU NEED HERE)
    def _encode_pixel(self, pos, number):
        """Hide a number from 0 to 999 in the last digits of pixel pos.

        If replacing a color's last digit would exceed 255, subtract 10;
        this preserves the digit and keeps the component in range.

        Parameter pos: the position in the flattened pixel list
        Precondition: pos is an int, 0 <= pos < image length

        Parameter number: the number to hide
        Precondition: number is an int in 0..999
        """
        assert isinstance(pos, int) and 0 <= pos < self.getCurrent().getLength()
        assert isinstance(number, int) and 0 <= number <= 999
        pixel = self.getCurrent().getFlatPixel(pos)
        digits = (number // 100, (number // 10) % 10, number % 10)
        result = []
        for component, digit in zip(pixel, digits):
            value = (component // 10) * 10 + digit
            if value > 255:
                value -= 10
            result.append(value)
        self.getCurrent().setFlatPixel(pos, tuple(result))
