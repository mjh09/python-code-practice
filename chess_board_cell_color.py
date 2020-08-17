def chessBoardCellColor(cell1, cell2):
    """
    Checks if two specificed chess board cells are the same color by
    constructing a dictionary representation of a board.

    Parameters:
        cell1 (string) : a string representation of a chess board cell [a-h1-8]
        cell2 (string) : a string representation of a chess board cell [a-h1-8]

    Returns:
        Bool
    """
    
    cb = {}
    letters = ['A','B','C','D','E','F','G','H']
    counter2 = 1     # used as a switch to determine the starting color

    for letter in letters:
        counter = 1  # specifies the current row number

        while counter < 9: # max rows of a chess board is 8
    
            if counter2 == 2:
                cb.update({f'{letter}{counter}':'black' if counter%2 == 0 else 'white'})
            else:
                cb.update({f'{letter}{counter}':'white' if counter%2 == 0 else 'black'})
            
            counter +=1
        
        
        if counter2 == 1: # switching between starting color
            counter2 = 2
        else:
            counter2 = 1
    
    c1c = cb[cell1]
    c2c = cb[cell2]
    
    return c1c == c2c 