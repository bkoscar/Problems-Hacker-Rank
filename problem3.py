"""
The provided code stub reads two integers, a and b, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,
a//b . The second line should contain the result of float division, a/b . 

"""

def division_numbers(a:int, b:int):
    if b ==0:
        raise ValueError("The number b can't be zero")
    else:
        integer_division = a // b
        float_division =  a / b
        print(integer_division)
        print(float_division) 


if __name__ == '__main__':
    a = int(input( ))
    b = int( input( ))
    division_numbers(a,b)