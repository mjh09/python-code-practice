def evenDigitsOnly(n):
    """ 
    Checks if all digits in a number are even

    Parameters:
        n (int) : a number

    Returns:
        Boolean : denotes whether all digits are even/odd

    """
    # reducing big numbers to the unique elements
    ints = set(list(str(n)))
    
    # applying a function to an iterable that reduces each value to its remainder after division
    modulo = map(lambda x: int(x) % 2, ints)
    
    # if any remainder after modulo, is odd
    if sum(list(modulo)) != 0:
        return False
    
    return True
