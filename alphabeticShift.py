def alphabeticShift(inputString):
    """
    Increments all the alphabetic characters in a string by one: end -> begin; (a->b)(z->a)

    Parameters:
        inputString (string) : a string of alphabetic characters

    Returns:
        "".join(char_lst) : incremented alphabetic string
    """

    char_lst = list(inputString)

    for idx, char in enumerate(char_lst):
        if char == 'z':                    # single edge case z -> a to hardcode
            char_lst[idx] = chr(ord('a'))
        else:
            replacement = chr(ord(char) + 1) # using unicode integer representation to increment
            char_lst[idx] = replacement
    
    return "".join(char_lst)