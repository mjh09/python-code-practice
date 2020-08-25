def extractEachKth(inputArray, k):
    """
    Returns a list with the kth elements removed

    Parameters:
        inputArray (array) : an array
        k (int) : the index step to remove

    Returns:
        result (arrary): new array without kth elements
    """
    
    result = []
    cnt = k - 1
    for elem in inputArray:
        if cnt > 0:
            cnt -= 1
            result.append(elem)
        else:
            cnt = k - 1
    return result
