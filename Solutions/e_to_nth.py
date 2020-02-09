
"""Print value of e to user-supplied precision.

    Usage:
        Runs from command line and prompts user for integer between 0 and 1000.
        Prints e to specified precision with no rounding.
"""

from decimal import Decimal as D, getcontext
from math import factorial


def calc_e(precision):
    """Returns a Decimal value for e to specified number of digits, without rounding

            Args:
                precision: number of digits to return after the decimal point
    """
    getcontext().prec = precision + 3
    e_prev = 1
    n = 1
    limit = 500
    while n <= limit:
        denom = D(factorial(n))
        e_calc = e_prev + 1 / denom
        if e_prev == e_calc:
            return D(str(e_calc)[0:-2])
        e_prev = e_calc
        n += 1
    


if __name__ == "__main__":
    """Prompts the user for an integer between 0 and 1000 and prints e to the specified number of digits after the decimal point"""
    while True:
        num = input("Please enter the precision you want:")
        if num.isdigit() and int(num) <= 1000:
            num = int(num)
            my_e = str(calc_e(num))
            print("e is approximately", my_e)
            break
        print("Please enter an integer between 0 and 1000.")

