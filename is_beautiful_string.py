def isBeautifulString(inputString):
    """
    Determines if each letter in a string satisfies the condition of
        appears at most as many times as its previous letter in the
        alaphabet. 'a' has no previous. e.g. 'bbc' = False <- no 'a'
        -> 'aabbc' = True 

    Parameters:
        inputString (str): a string

    Returns:
        Bool
    """
    # Being too clever and hard to read
    cnts = {letter: inputString.count(letter) for letter in set(inputString)}
    
    is_beautiful = {x: cnts[x] <= [cnts[chr(ord(x) - 1)] if chr(ord(x) - 1) in cnts.keys() else 0][0] if x != 'a' else True for x in cnts.keys()}
    
    return all(is_beautiful.values())