def arrayMaximalAdjacentDifference(inputArray):
    ''' Returns maximal absolute difference of adjacent integers in an array

        Parameters :
            inputArray (array) : Array of integers

        Returns:
            maximum : Integer 

    '''
        
    maximum = 0
    
    first = None
    
    for number in inputArray:
        
        if isinstance(first, int):
            
            abs_dif = abs(number - first)
            
            if abs_dif > maximum:
                maximum = abs_dif
                first = number
            
            else:
                first = number
                
        else:
            first = number
    
    return maximum