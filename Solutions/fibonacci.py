
"""Print first n values of Fibonacci sequence.

    Usage:
        Runs from command line and prompts user for integer n between 0 and 1000.
        Prints first n members of the Fibonacci sequence .
"""


def fibonacci(num):
    """Returns a list of the first num members of the Fibonacci sequence

            Args:
                num: number of members to return
    """
    sequence = [0, 1]
    if num <= 2:
        return sequence[0:num]
    c = 0
    while len(sequence) < num:
        sequence.append(sequence[c] + sequence[c + 1])
        c += 1
    return sequence  


def print_fibonacci(num):
    """Prints the first [num] Fibonacci numbers

        Args:
            num: number of Fibonacci numbers to return
    """
    print(fibonacci(num))


if __name__ == "__main__":
    """Prompts the user for an integer n between 0 and 1000 and prints a list of the first n numbers in the Fibonacci sequence"""
    while True:
        num = input("Please enter how many Fibonacci numbers you want:")
        if num.isdigit() and int(num) <= 1000:
            num = int(num)
            print_fibonacci(num)
            break
        print("Please enter an integer between 0 and 1000.")

