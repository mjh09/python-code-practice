def arrayMaxConsecutiveSum(inputArray, k):
    """
    Sums and returns largest value of contiguous subsets in an array.

        Parameters:
            inputArray (array) : array of integers
            k (int) : length of subset

        Returns:
            result (int) : largest sum of subset
    """
    if k == 1:
      return max(inputArray)
    
    sub = inputArray[0:k]
    largest = sum(sub)
    result = largest
    
    for val in inputArray[k:]:
        largest -= sub[0]
        sub.remove(sub[0])
        sub.append(val)
        largest += val
        
        if largest > result:
            result = largest

    return result