def depositProfit(deposit, rate, threshold):
    """
    Calulates the amount of years it will take a deposit amount
    to reach a threshold givne a specified growth rate

    Parameters:
        deposit (int) : intial starting amount
        rate (int) : integer representation of the percent rate
        threshold (int) : the target amount

    Returns:
        years (int) : amount of years to reach threshold at given rate
    """

    total = deposit
    years = 0
    
    while total < threshold:
        total = total + (total * (rate * .01)) # Calculate the growth per year and add to current total
        years += 1
    
    return years