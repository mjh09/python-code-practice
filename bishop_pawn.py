def bishopAndPawn(bishop, pawn):
    """
    Determines if a pawn is in range of a bishop

    Parameters:
        bishop (str) : letter/number coordinate ('a1')
        pawn (str) : letter/nuber coordinate ('b2')

    Returns:
        Bool
    """
    bish, paw = list(bishop), list(pawn)
    letter_range = abs(ord(bish[0]) - ord(pawn[0]))
    num_range = abs(int(bish[1]) - int(paw[1]))
    
    if letter_range == num_range:
      return True
     
    return False