"""

The provided code stub reads two integers a, b from STDIN, and

Add code to print three lines where:

1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers (first - second).
3. The third line contains the product of the two numbers.

"""


def sum_numbers(a:int, b:int ):
    """This function calculate the sum, substraction and multiplication of two integer numbers.

    Args:
        a (int): integer number
        b (int): integer number
    """
    suma = a + b 
    substraction = a - b
    multiplication = a * b 
    print(suma)
    print(substraction)
    print(multiplication) 

if __name__ == '__main__':
    a = int(input( ))
    b = int(input( ))
    sum_numbers(a,b)