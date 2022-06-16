# Leap year problem

def is_leap(year:int):
    """This function  given a year return when is a year leap

    Args:
        year (int): Year

    Returns:
        Boolean: When a year is a year leap
    """
    leap = True
    if year % 4 == 0:
        if year % 100 == 0:
            if year% 400 == 0:
                return leap 
            return not leap
        return leap
    else:
        return not leap 


if __name__ == '__main__':
    year = int(input( ))
    print(is_leap(year))