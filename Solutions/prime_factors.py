
"""Calculates prime factors of a given number

    Usage:
        Runs from command line and prompts user for an integer.
        Prints all prime factors.
"""


def get_primes(max):
    """Returns all prime numbers up to and including [max]

        Args:
            max: highest number to be returned. If [max] is prime, list is inclusive.
    """
    primes = [2, 3]
    c = 2
    while primes[-1] <= max:
        next = primes[-1] + c
        if next > max:
            break
        is_prime = True
        for prime in primes:
            if next % prime == 0:
                is_prime = False
                c +=2
                break
        if is_prime:
            primes.append(next)
            c = 2
    return primes


def prime_factors(num):
    """Returns a list of the prime factors for user-supplied integer

            Args:
                num: integer for which to find prime factors.
    """
    primes = get_primes(num)
    factors = []
    for prime in primes:
        while num % prime == 0:
            factors. append(prime)
            num = num // prime
    return factors


def print_primes(num):
    """Prints the prime factors of [num]

        Args:
            num: integer for which to print prime factors
    """
    print(prime_factors(num))


if __name__ == "__main__":
    """Prompts the user for an integer and prints a list of the prime factors"""
    while True:
        num = input("Please enter an integer, and I'll return the prime factors:")
        if num.isdigit():
            num = int(num)
            print_primes(num)
            break
        print("Please enter a positive integer.")

