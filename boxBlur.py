def boxBlur(image):
    """ Reduces a matrix to sub-matrix average of 3x3 intervals aka box blur algorithm

        Parameters:
            image (matrix): 3x3 array or greater

        returns:
            result (matrix) : reduced matrix
    """

    s1 = len(image[0])
    if s1 > 3:
        column = 1 + (s1 - 3)
    else:
        column = 1

    s2 = len(image)
    if s2 > 3:
        rows = 1 + (s2 - 3)
    else:
        rows = 1

    m1, m2, m3 = 0, 1, 2
    slice1 = 0
    slice2 = 3
    result = []

    while rows > 0:
        cur_avg = []
        sections = column
    
        while sections > 0:
            mat_avr  = int(sum(image[m1][slice1:slice2] \
                        + image[m2][slice1:slice2] \
                        + image[m3][slice1:slice2]) \
                        / 9 )
    
            cur_avg.append(mat_avr)
            slice1 += 1
            slice2 += 1
            sections -= 1

    
        result.append(cur_avg)
        slice1 = 0
        slice2 = 3
        m1 += 1
        m2 += 1
        m3 += 1
        rows -= 1
    
    return result