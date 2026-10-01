""" 
Functions for Assignment A3

This file contains the functions for the assignment. You should replace the 
stubs with your own implementations.

YOUR NAME(S) AND NETID(S) HERE
DATE COMPLETED HERE
"""
import introcs
import math


def complement_rgb(rgb):
    """
    Returns the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    # THIS IS WRONG. FIX IT; I fixed it bro calm down all caps for what
    return introcs.RGB(255-rgb.red, 255-rgb.green, 255-rgb.blue)


def str5(value):
    """
    Returns value as a string, but expanded or rounded to be exactly 5 characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
    
    Parameter value: the number to conver to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    # Remember that the rounding takes place at a different place depending 
    # on how big value is. Look at the examples in the specification.

    if value >= 100:
        val = round(value, 1)
    elif value >= 10:
        val = round(value, 2)
    else:
        val = round(value, 3)
    val = str(float(val))

    if len(val) == 4:
        val = val + '0'
    elif len(val) == 3:
        val = val + '00'
    return str(val)
    
def str5_cmyk(cmyk):
    """
    Returns the string representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces 
    after the commas. These must be there.
    
    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    val = str5(cmyk.cyan) + ', ' + str5(cmyk.magenta) + ', ' + str5(cmyk.yellow) + ', ' + str5(cmyk.black)
    return '(' + val + ')'


def str5_hsl(hsl):
    """
    Returns the string representation of hsl in the form "<H, S, L>".
    
    In the output, each of H, S, and L should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsl)
    
    Example: if str(hsl) is 
    
          '<0.0,0.313725490196,0.5>'
    
    then str5_hsl(hsl) is '<0.000, 0.314, 0.500>'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsl: the color to convert to a string
    Precondition: hsl is an HSL object.
    """
    value = '<' + str5(hsl.hue) + ', ' + str5(hsl.saturation) + ', ' + str5(hsl.lightness) + '>'
    return value


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.
    
    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to the range 0..1 by dividing them by 255.0.
    pass


def cmyk_to_rgb(cmyk):
    """
    Returns an RGB object equivalent to cmyk
    
    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # The CMYK numbers are in the range 0.0..100.0. 
    # Deal with them the same way as the RGB numbers in rgb_to_cmyk()
    pass


def rgb_to_hsl(rgb):
    """
    Returns an HSL object equivalent to rgb
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
   
    Parameter rgb: the color to convert to an HSL object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    pass


def hsl_to_rgb(hsl):
    """
    Returns and RGB object equivalent to hsl
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
    
    Parameter hsl: the color to convert to a RGB object
    Precondition: hsl is an HSL object.
    """
    pass


def contrast_value(value,contrast):
    """
    Returns value adjusted to the "sawtooth curve" for the given contrast
    
    At contrast = 0.5, the curve is the normal line y = x, so value is 
    unaffected. If contrast < 0.5, values are pulled closer together, with all 
    values collapsing to 0.5 when contrast = 0. If contrast > 0, the values are 
    pulled farther apart, with all values becoming 0 or 1 when contrast = 1.
    
    Parameter value: the value to adjust
    Precondition: value is a float in 0..1
    
    Parameter contrast: the contrast amount (0.5 is no contrast)
    Precondition: contrast is a float in 0..1
    """
    pass


def contrast_rgb(rgb,contrast):
    """
    Applies the given contrast to the RGB object rgb
    
    This function is a PROCEDURE. It modifies rgb and has no return value. It 
    should apply contrast_value to the red, blue, and green values.
    
    Parameter rgb: the color to adjust
    Precondition: rgb is an RGB object
    
    Parameter contrast: the contrast amount (0.5 is no contrast)
    Precondition: contrast is a float in 0..1
    """
    pass
