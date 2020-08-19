def absoluteValuesSumMinimization(a):
    """
    Given an array of sorted integers, finds the integer with the
    smallest total abs value from every other element

    Parameters:
        a (array) : array of integers
    
    Returns:
        res[0] (int) : the element with the smallest total abs value
                       from every other elem
    """
    # # using median
    # len_a = len(a)
    # if len_a % 2 ==0:
    #     return a[(len_a // 2) - 1]
    # return a[len(a)//2]
    
    # using map
    results = {}
    for elem in a:
        res = map(lambda x: abs(elem - x), a)
        results[elem] = sum(list(res))

    min_val = min(results.values()) 
    res = [key for key in results if results[key] == min_val]
    return res[0] 