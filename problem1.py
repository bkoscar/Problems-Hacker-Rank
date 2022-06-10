# Main Module

class Number:
    """ This class represent an integer number.
    Attributes:
        n (int): Integer number
    """
    
    def __init__(self, n:int):
        """Initialize in an objet of type integer

        Args:
            n (int): Integer number
        """
        self.n = n 

        
    def is_weird(self):
        """ If the number is even or odd  and satisfy certain conditions return Wierd or Not Wierd

        Returns:
           string
        """
        if self.n % 2 != 0:
            return "Weird"
        elif self.n % 2 == 0 and 2 <= self.n <= 5:
            return "Not Weird"
        elif self.n % 2 == 0 and 6 <= self.n <= 20:
            return "Weird"
        elif self.n % 2 == 0 and 20 < self.n:
            return "Not Weird"



if __name__ == '__main__':
    """
    Example
    -------
    >>> n = 3
    >>> number = Number(n)
    >>> print(number.is_weird())
    >>> Weird
        
    """
    n = int(input())
    number = Number(n)
    print(number.is_weird())