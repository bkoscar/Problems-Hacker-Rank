"""

The provided code stub reads and integer, , from STDIN. For all non-negative integers i < n, print i**2


"""

def square_number(n:int):
    """This function given a integer number return all square integers less than n

    Args:
        n (int): integer number
    """
    for i in range(n):
        print(i**2)




if __name__ == '__main__':
    n = int( input ( ))
    square_number(n)