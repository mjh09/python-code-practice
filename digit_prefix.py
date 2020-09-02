def longestDigitsPrefix(inputString):
    """
    Returns the numeric prefix of a string if present

    Parameters:
        inputString (str)

    Returns:
        current (str) : numeric prefix or empty
    """

    current = ''
    previous = None
    
    for elem in inputString:
        
        is_digit = ord(elem) in range(48, 58) # "0" -> "9" 
        
        if is_digit:
            current += elem
            previous = elem
            continue
        
        elif previous:
            return current
            
        else:
            return current

    return current