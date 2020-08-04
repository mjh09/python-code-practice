
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    ''' Determines if the min and max values for your/friends left/right are equal

        Parameters:
            yourLeft (positive integer)
            yourRight (positive integer)
            friendsLeft (positive integer)
            friendsRight (positive integer)

        Returns:
            Boolean
    '''
    yours = [yourLeft, yourRight]
    your_strongest = max(yours)
    your_weakest = min(yours)
    
    friends = [friendsLeft, friendsRight]
    friends_strongest = max(friends)
    friends_weakest = min(friends)
    
    if your_strongest == friends_strongest:
        if your_weakest == friends_weakest:
            return True
    
    return False