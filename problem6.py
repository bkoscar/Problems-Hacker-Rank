# Print Function

def blank_spaces(n: int):
    """This function given a integer number n print all
    numbers concatenated from 1 to n

    Args:
        n (int): integer number
    """
    for i in range(1, n+1, 1):
        print(i, end='')


if __name__ == '__main__':
    n = int(input())
    blank_spaces(n)
