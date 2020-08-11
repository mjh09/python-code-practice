def arrayReplace(inputArray, elemToReplace, substitutionElem):
    """
    Substitutes all specified elements in an array

    Parameters:
        inputArray (array) : array 
        elemToReplace (not specified) : some character
        substitutionElem (not specified) : some character

    Returns:
        inputArray (array) : modified input
    """
    
    for idx, elem in enumerate(inputArray):
        if elem == elemToReplace:
            inputArray[idx] = substitutionElem
            
    return inputArray