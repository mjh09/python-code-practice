def avoidObstacles(inputArray):
    """ Determines the least possible value to avoid intersectoions between two sets

        Parameters:
            inputArray (array) : array of integers denoting obstacles

        Returns:
            min_step (integer) : minimum possible step interval that avoids collision with input

    """

    max_step = max(inputArray) + 1
    
    min_step = 1
    
    obstacles = set(inputArray)
    
    while min_step < max_step:
        steps = set(range(0, max_step + 1, min_step))
        
        collisions = len(set.intersection(steps, obstacles))
        
        if collisions < 1:
            return min_step
        
        else:
            min_step += 1
            
    return min_step