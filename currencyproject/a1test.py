"""
Test script for module a1

When run as a script, this module invokes several procedures that 
test the various functions in the module a1.

Author: Avi Sharma as4632
Date:   09/11/2026
"""

import introcs
import a1

def testA():
    """
    Test procedure for Part A
    """
    # Test before_space
    introcs.assert_equals("USD", a1.before_space("USD  100"))
    introcs.assert_equals("EUR", a1.before_space("EUR 50"))
    introcs.assert_equals("USD", a1.before_space("USD 100 extra"))
    introcs.assert_equals("", a1.before_space(" USD"))

    # Test after_space
    # Testing Double Space
    introcs.assert_equals(" 100", a1.after_space("USD  100"))
    introcs.assert_equals("50", a1.after_space("EUR 50"))
    introcs.assert_equals("100 extra", a1.after_space("USD 100 extra"))
    introcs.assert_equals("USD", a1.after_space(" USD"))


def testB():
    """
    Test procedure for Part B
    """
    # Test get_old with a valid query
    json = ('{"err":"","old":"1 Bitcoin",' +
            '"new":"69190.992850277 Euros","valid":true}')
    introcs.assert_equals("1 Bitcoin", a1.get_old(json))

    # Test get_old with another valid query
    json = '{"err":"","old":"2 US Dollars","new":"1.72 Euros","valid":true}'
    introcs.assert_equals("2 US Dollars", a1.get_old(json))

    # Test get_old with an invalid query
    json = ('{"err":"Currency amount is invalid.",' +
            '"old":"","new":"","valid":false}')
    introcs.assert_equals("", a1.get_old(json))

    # Test get_new with a valid query
    json = ('{"err":"","old":"1 Bitcoin",' +
            '"new":"69190.992850277 Euros","valid":true}')
    introcs.assert_equals("69190.992850277 Euros", a1.get_new(json))

    # Test get_new with another valid query
    json = '{"err":"","old":"2 US Dollars","new":"1.72 Euros","valid":true}'
    introcs.assert_equals("1.72 Euros", a1.get_new(json))

    # Test get_new with an invalid query
    json = ('{"err":"Currency amount is invalid.",' +
            '"old":"","new":"","valid":false}')
    introcs.assert_equals("", a1.get_new(json))

    # Test has_error with a valid query
    json = ('{"err":"","old":"1 Bitcoin",' +
            '"new":"69190.992850277 Euros","valid":true}')
    introcs.assert_equals(False, a1.has_error(json))

    # Test has_error with another valid query
    json = '{"err":"","old":"2 US Dollars","new":"1.72 Euros","valid":true}'
    introcs.assert_equals(False, a1.has_error(json))

    # Test has_error with an invalid query
    json = ('{"err":"Currency amount is invalid.",' +
            '"old":"","new":"","valid":false}')
    introcs.assert_equals(True, a1.has_error(json))


def testC():
    """
    Test procedure for Part C
    """
    # Test valid query
    json = a1.query_website('USD', 'EUR', 2.5)
    expected = ('{ "err":"", "old":"2.5 United States Dollars", ' +
                '"new":"2.1526975 Euros", "valid":true }')
    introcs.assert_equals(expected, json)

    # Test invalid query
    json = a1.query_website('AAA', 'EUR', 2.5)
    expected = ('{ "err":"Source currency code is invalid.", ' +
                '"old":"", "new":"", "valid":false }')
    introcs.assert_equals(expected, json)


def testD():
    """
    Test procedure for Part D
    """
    # Test is_currency
    introcs.assert_equals(True, a1.is_currency('USD'))
    introcs.assert_equals(True, a1.is_currency('EUR'))
    introcs.assert_equals(True, a1.is_currency('CUP'))
    introcs.assert_equals(False, a1.is_currency('AAA'))
    introcs.assert_equals(False, a1.is_currency('ZZZ'))

    # Test exchange (using assert_floats_equal)
    introcs.assert_floats_equal(2.1526975, a1.exchange('USD', 'EUR', 2.5))
    eur_to_usd = a1.exchange('EUR', 'USD', 10.0)
    introcs.assert_floats_equal(11.613336290863, eur_to_usd)
    introcs.assert_floats_equal(1.0, a1.exchange('USD', 'USD', 1.0))

testA()
testB()
testC()
testD()
print('Module a1 passed all tests.')