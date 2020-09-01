def min_weight_max_val(value1, weight1, value2, weight2, maxW):
    """
    Determines the maximum value possible of two items under a threshold

        Parameters:
            value1 (int)
            weight1 (int)
            value2 (int)
            weight2 (int)
            maxW (int) : weight threshold to not exceed
        
        Returns:
            value1 | value2 | 0 
    """
    
    if (weight1 + weight2) <= maxW:   
        return value1 + value2
    
    elif weight1 <= maxW:    
        if weight2 <= maxW:
            if value2 > value1:
                return value2
        return value1
    
    elif weight2 <= maxW:
        return value2
    
    return 0
