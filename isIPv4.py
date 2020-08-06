def isIPv4Address(inputString):
    ''' Checks if string is a valid IPv4 address #noqa

        Parameters:
            inputString (str): Ideally a valid IPv4

        Returns:
            Bool

    '''

    #Checking for proper decimal notation
    syntax = inputString.count('.')
    
    if syntax != 3:
        return False 
        
    
    #Extracting numbers
    nums = inputString.split('.')
    
    for num in nums:
        
        if len(num) > 1:
            if num.startswith('0'):   #Leading zeros bad
                return False
        try:                         
            num  = int(num)          
            
            if isinstance(num, int):
                if num > 255:         
                    return False
        except:
            return False
        
            
    return True