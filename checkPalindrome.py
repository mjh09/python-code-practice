def checkPalindrome(inputString):
    if len(inputString) % 2 == 0:
        first_mid = len(inputString) // 2
        second_mid = first_mid
    
    else:
        first_mid = len(inputString) // 2
        second_mid = len(inputString) // 2 + 1

    half1 = inputString[:first_mid]
    half2 = inputString[second_mid:]
    half2 = half2[::-1]

    if half1 == half2:
        return True
    else:
        return FalseS