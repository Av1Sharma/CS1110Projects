"""
Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange.

Author: Avi Sharma as4632 Kosta Nani kn464
Date:   09/16/2026
"""


import introcs


def is_currency(code):
    """
    Returns: True if code is a valid (3 letter code for a) currency
    It returns False otherwise.

    Parameter code: the currency code to verify
    Precondition: code is a string with no spaces or non-letters.
    """
    json = query_website(code, code, 1.0)
    return not has_error(json)


def exchange(src, dst, amt):
    """
    Returns the amount of currency received in the given exchange.
    
    In this exchange, the user is changing amt money in currency 
    src to the currency dst. The value returned represents the 
    amount in currency dst.
    
    The value returned has type float.
    
    Parameter src: the currency on hand
    Precondition: src is a string for a valid currency code
    
    Parameter dst: the currency to convert to
    Precondition: dst is a string for a valid currency code
    
    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    json = query_website(src, dst, amt)
    new_str = get_new(json)
    amt_str = before_space(new_str)
    return float(amt_str)


def before_space(s):
    """
    Returns a copy of s up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    
    first_space = s.index(" ")
    return s[:first_space]

def after_space(s):
    """
    Returns a copy of s after the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    
    first_space = s.index(" ")
    return s[first_space+1:]

def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quotes

    A quote character is one that is inside a string, not one that 
    delimits it.  We typically use single quotes (') to delimit a 
    string if want to use a double quote character (") inside of it.

    Examples:
    first_inside_quotes('A "B C" D') returns 'B C'
    first_inside_quotes('A "B C" D "E F" G') returns 'B C', 
    because it only picks the first such substring

    Parameter s: a string to search
    Precondition: s is a string containing at least two double quotes
    """
    start = s.index('"')
    end = s.index('"', start+1)
    return s[start+1:end]

def get_old(json):
    """
    Returns the original value in the response to a currency query

    Given a JSON response to a currency query, this returns the 
    string inside double quotes (") immediately following the keyword
    "old". For example, if the JSON is
        
    '{ "err":"", "old":"1 Bitcoin", "new":"69190.992850277 Euros", "valid":true }'

    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').  

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """

    start = json.index('"old"') + len('"old"')+1
    return first_inside_quotes(json[start:])


    
    
def get_new(json):
    """
    Returns the converted value in the response to a currency query

    Given a JSON response to a currency query, this returns the 
    string inside double quotes (") immediately following the keyword
    "new". For example, if the JSON is

    '{ "err":"", "old":"1 Bitcoin", "new":"69190.992850277 Euros", "valid":true }'

    then this function returns '69190.992850277 Euros' (not 
    '"69190.992850277 Euros"').  

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    start = json.index('"new"') + len('"new"')+1
    return first_inside_quotes(json[start:])

def has_error(json):
    """
    Returns True if the query has an error; False otherwise.

    Given a JSON response to a currency query, this returns the 
    opposite of the value following the keyword "valid". For example,
    if the JSON is 

    '{ "err":"Currency amount is invalid.", "old":"", "new":"", "valid":false }'

    then the query is not valid, so this function returns True (It 
    does NOT return the message 'Source currency code is invalid').

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    pos = json.find('"valid":')
    value = json[pos + 8:pos + 13]
    return value == 'false'

def query_website(src, dst, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the 
    currency dst. The response should be a string of the form    

    '{ "err":"", "old":"<old-amt>", "new":"<new-amt>", "valid":true }'

    where the values old-amount and new-amount contain the value 
    and name for the original and new currencies. If the query is 
    invalid, both old-amount and new-amount will be empty, while 
    "valid" will be followed by the value false (and "err" will have 
    an error message).

    Parameter src: the currency on hand
    Precondition: src is a string with no spaces or non-letters
        
    Parameter dst: the currency to convert to
    Precondition: dst is a string with no spaces or non-letters
        
    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    url = 'http://cs1110.cs.cornell.edu/2026fa/a1?src=' + src
    url = url + '&dst=' + dst
    url = url + '&amt=' + str(amt)

    return introcs.urlread(url)




    

