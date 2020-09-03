def digitDegree(n):
    """
    Returns the amount of steps it takes to reduce a numbers digits to 
    a single digit (e.g 901 -> 1: (9 + 0 + 1 = 10) -> 2: (1 + 0 = 1)

    Parameters:
        n (int): a number

    Returns
        cnt (int): the number of steps to reduction
    """

    dig_str = str(n)
    digs = list(dig_str)
    cnt = 0
    
    while len(digs) > 1:
        digs = sum([int(x) for x in digs])
        digs = list(str(digs))
        cnt += 1
    
    return cnt