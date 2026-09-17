"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and
an amount. It prints out the result of converting the first currency to
the second.

Author: Avi Sharma (as4632), Kosta Nani (kn464)
Date:   09/16/2026
"""

import a1


org = input('Enter original currency: ')
desired = input('Enter desired currency: ')
amt = float(input('Enter original amount: '))

result = a1.exchange(org, desired, amt)

print('You can exchange ' + str(amt) + ' ' + org +
      ' for ' + str(result) + ' ' + desired + '.')