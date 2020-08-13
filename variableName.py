def variableName(name):
    """
    Checks if each character in a string is an allowed character ([azAZ][0-9][_]) and 
    does not start with a integer.
    
        Parameters:
            name (string) : string of characters

        Returns:
            Boolean : allowable or no

    """

    name_chars = list(name)
    
    if ord(name_chars[0]) in range(48, 58):
            return False
    
    allowed = set()
    allowed.update(range(48,58))    # integer representation of unicode of integers 
    allowed.update(range(65, 91))   # integer representation of unicode of upper alphabet 
    allowed.update(range(97, 123))  # integer representation of unicode of lower alphabet 
    allowed.add(95)                 # integer representation of unicode of '_' 
    
    for char in name:
        if ord(char) in allowed:
            continue
        else:
            return False
            
    return True