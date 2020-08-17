def circleOfNumbers(n, firstNumber):
    """
    Finds the polar opposite of firstNumber on an equally distributed
    circle of numbers (eg clock). Must be of even length.

    Parameters:
        n (int): denotes length of numbers eg 0 to n-1
        firstNumber (int): references one side of polar coordinates.

    Returns:
        Opposite polar coordinate of firstNumber
    """

    half = int(n/2)
    
    if firstNumber > half:
        return firstNumber - half # go backward 
    
    elif firstNumber < half:
        return firstNumber + half # go forward
    
    else:
        return 0 # opposite of middle num is always 0
    