"""
Test script for module a1

When run as a script, this module invokes several procedures that
test the various functions in the module a1.

Author: Avi Sharma (as4632), Kosta Nani (kn464)
Date:   09/16/2026
"""

import introcs
import a1


def testA():
    """
    Test procedure for Part A.

    Tests the functions before_space and after_space in module a1.
    """
    # Test before_space with double space between words
    introcs.assert_equals("USD", a1.before_space("USD  100"))

    # Test before_space with a single space between words
    introcs.assert_equals("EUR", a1.before_space("EUR 50"))

    # Test before_space with multiple words after the space
    introcs.assert_equals("USD", a1.before_space("USD 100 extra"))
    
    # Test before_space with trailing space (space at the end)
    introcs.assert_equals("USD", a1.before_space("USD "))

    # Test before_space with leading space (space at the beginning)
    introcs.assert_equals("", a1.before_space(" USD"))

    # Test after_space with double space between words
    introcs.assert_equals(" 100", a1.after_space("USD  100"))

    # Test after_space with a single space between words
    introcs.assert_equals("50", a1.after_space("EUR 50"))

    # Test after_space with multiple words after the space
    introcs.assert_equals("100 extra", a1.after_space("USD 100 extra"))

    # Test after_space with leading space (space at the beginning)
    introcs.assert_equals("USD", a1.after_space(" USD"))

    # Test after_space with trailing space (space at the end)
    introcs.assert_equals("", a1.after_space("USD "))


def testB():
    """
    Test procedure for Part B.

    Tests the functions first_inside_quotes, get_old, get_new, and
    has_error in module a1.
    """
    # Test first_inside_quotes with substring in middle of string
    introcs.assert_equals('B C', a1.first_inside_quotes('A "B C" D'))

    # Test first_inside_quotes with multiple pairs of double quotes
    introcs.assert_equals('B C', a1.first_inside_quotes('A "B C" D "E F" G'))

    # Test first_inside_quotes with quotes at start and end of string
    introcs.assert_equals('hello', a1.first_inside_quotes('"hello"'))

    # Test first_inside_quotes with empty string between quotes
    introcs.assert_equals('', a1.first_inside_quotes('before "" after'))

    # Test get_old with a valid query
    json = ('{"err":"","old":"1 Bitcoin",' +
            '"new":"69190.992850277 Euros","valid":true}')
    introcs.assert_equals("1 Bitcoin", a1.get_old(json))

    # Test get_old with another valid query
    json = ('{ "err":"", "old":"2.5 United States Dollars", ' +
            '"new":"64.375 Cuban Pesos", "valid":true }')
    introcs.assert_equals("2.5 United States Dollars", a1.get_old(json))

    # Test get_old with an invalid query
    json = ('{"err":"Currency amount is invalid.",' +
            '"old":"","new":"","valid":false}')
    introcs.assert_equals("", a1.get_old(json))

    # Test get_new with a valid query
    json = ('{"err":"","old":"1 Bitcoin",' +
            '"new":"69190.992850277 Euros","valid":true}')
    introcs.assert_equals("69190.992850277 Euros", a1.get_new(json))

    # Test get_new with another valid query
    json = ('{ "err":"", "old":"2.5 United States Dollars", ' +
            '"new":"64.375 Cuban Pesos", "valid":true }')
    introcs.assert_equals("64.375 Cuban Pesos", a1.get_new(json))

    # Test get_new with an invalid query
    json = ('{"err":"Currency amount is invalid.",' +
            '"old":"","new":"","valid":false}')
    introcs.assert_equals("", a1.get_new(json))

    # Test has_error with a valid query
    json = ('{"err":"","old":"1 Bitcoin",' +
            '"new":"69190.992850277 Euros","valid":true}')
    introcs.assert_equals(False, a1.has_error(json))

    # Test has_error with another valid query
    json = ('{ "err":"", "old":"2.5 United States Dollars", ' +
        '"new":"64.375 Cuban Pesos", "valid":true }')
    introcs.assert_equals(False, a1.has_error(json))

    # Test has_error with an invalid query
    json = ('{"err":"Currency amount is invalid.",' +
            '"old":"","new":"","valid":false}')
    introcs.assert_equals(True, a1.has_error(json))


def testC():
    """
    Test procedure for Part C.

    Tests the function query_website in module a1.
    """
    # Test query_website with valid query
    json = a1.query_website('USD', 'EUR', 2.5)
    expected = ('{ "err":"", "old":"2.5 United States Dollars", ' +
                '"new":"2.1526975 Euros", "valid":true }')
    introcs.assert_equals(expected, json)

    # Test query_website with invalid source currency query
    json = a1.query_website('AAA', 'EUR', 2.5)
    expected = ('{ "err":"Source currency code is invalid.", ' +
                '"old":"", "new":"", "valid":false }')
    introcs.assert_equals(expected, json)

    # Test query_website with another valid destination currency
    json = a1.query_website('USD', 'CUP', 2.5)
    expected = ('{ "err":"", "old":"2.5 United States Dollars", ' +
                '"new":"64.375 Cuban Pesos", "valid":true }')
    introcs.assert_equals(expected, json)

    # Test query_website with invalid destination currency
    json = a1.query_website('USD', 'AAA', 2.5)
    expected = ('{ "err":"Exchange currency code is invalid.", ' +
                '"old":"", "new":"", "valid":false }')

    # Test query_website with identical source and destination currency
    json = a1.query_website('USD', 'USD', 2.5)
    expected = ('{ "err":"", "old":"2.5 United States Dollars", ' +
                '"new":"2.5 United States Dollars", "valid":true }')
    introcs.assert_equals(expected, json)

def testD():
    """
    Test procedure for Part D.

    Tests the functions is_currency and exchange in module a1.
    """
    # Test is_currency with valid currency code USD
    introcs.assert_equals(True, a1.is_currency('USD'))

    # Test is_currency with valid currency code EUR
    introcs.assert_equals(True, a1.is_currency('EUR'))

    # Test is_currency with valid currency code CUP
    introcs.assert_equals(True, a1.is_currency('CUP'))

    # Test is_currency with invalid currency code AAA
    introcs.assert_equals(False, a1.is_currency('AAA'))

    # Test is_currency with invalid currency code ZZZ
    introcs.assert_equals(False, a1.is_currency('ZZZ'))

    # Test exchange from USD to EUR
    introcs.assert_floats_equal(2.1526975, a1.exchange('USD', 'EUR', 2.5))

    # Test exchange from EUR to USD
    eur_to_usd = a1.exchange('EUR', 'USD', 10.0)
    introcs.assert_floats_equal(11.613336290863, eur_to_usd)

    # Test exchange with identical source and destination currency
    introcs.assert_floats_equal(1.0, a1.exchange('USD', 'USD', 1.0))


testA()
testB()
testC()
testD()
print('Module a1 passed all tests.')