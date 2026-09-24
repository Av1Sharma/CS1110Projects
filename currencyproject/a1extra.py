"""
An extra function to add to Assignment 1

This module imports a1.py so it can access those functions as helpers.

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""
import a1


def expand_code(code):
    """
    Returns the full name of a currency from the currency code.

    The name of the code should be singular, not plural.

    Example: expand_code('USD') returns 'United States Dollar'
             expand_code('GBP') returns 'British Pound Sterling'

    Parameter code: the currency code
    Precondition: src is a string for a valid currency code
    """
    # Use the code in a currency query to the website
    # Then extract the name from the response
    json = a1.query_website(code, code, 1.0)

    return a1.get_new(json)[2:]
    ##string = json[json.find('1')+2:]
    ##return string[:string.find('"')]

print(expand_code('USD'))

# json = a1.query_website(code, code, 1.0)
# string = json[22:]
# return string[:string.find('"')]
##json = a1.query_website(code, code, 1.0)
##string = json[22:]
##return string[:string.find('"')]
