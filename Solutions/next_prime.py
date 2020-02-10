
"""Gives prime numbers until told to stop.

    Usage:
        Runs from command line and prompts user if they want the next prime.
        Yes means give me one.
        No means stop.
"""
from prime_factors import get_primes
import re


def get_next_prime(num):
    """Returns the prime number after [num]

        Args:
            num: prime number before the one to be returned
    """
    if num == 0:
        return 2
    elif num == 2:
        return 3
    primes = get_primes(num)
    c = 2
    is_prime = False
    while is_prime == False:
        next = num + c
        is_prime = True
        for prime in primes:
            if next % prime == 0:
                is_prime = False
                c +=2
        if is_prime:
            return next



if __name__ == "__main__":
    """Prompts the user if they want another prime"""
    current = 0
    while True:
        response = input("Do you want a prime number (y/n)?")
        if re.match('[yY][eE]?[sS]?', response):
            current = get_next_prime(current)
            print(current)
        else:
            print("Okay! I'll stop.")
            break

