
"""Print value of Pi to user-supplied precision.

    Usage:
        Runs from command line and prompts user for integer between 0 and 1000.
        Prints Pi to specified precision with no rounding.
"""

from decimal import Decimal as D, getcontext


def gauss_legendre(precision):
    """Returns a Decimal value for pi to specified number of digits, without rounding

            Args:
                precision: number of digits to return after the decimal point
    """
    getcontext().prec = precision + 2
    a0 = 1
    b0 = 1 / D(2).sqrt()
    t0 = D(.25)
    p0 = 1
    c = 1
    while c <= (precision // 2) + 1:
        an = (a0 + b0) / D(2)
        bn = D(a0 * b0).sqrt()
        tn = t0 - p0 * ((a0 - an) ** 2)
        pn = 2 * p0
        a0, b0, t0, p0 = an, bn, tn, pn
        c += 1
    pi_calc = ((an + bn) ** D(2)) / (4 * tn)
    return D(str(pi_calc)[0:-1])


if __name__ == "__main__":
    """Prompts the user for an integer between 0 and 1000 and prints pi to the specified number of digits after the decimal point"""
    while True:
        num = input("Please enter the precision you want:")
        if num.isdigit() and int(num) <= 1000:
            num = int(num)
            my_pi = str(gauss_legendre(num))
            print("Pi is approximately", my_pi)
            break
        print("Please enter an integer between 0 and 1000.")


