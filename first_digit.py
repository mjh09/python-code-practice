def firstDigit(inputString):
    """
    Finds and returns the first digit in a string

    Parameters:
        inputString (string) : a string

    Returns:
        elem (str) : the string representation of the first digit
    """
    
    str_lst = list(inputString)
    for elem in str_lst:
        try:
            int(elem)
            return elem
        except:
            continue