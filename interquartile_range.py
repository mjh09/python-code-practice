import math
### steps
numbers = [1,2,3,4,5,6,7,8,9,10,11]

## find median -> Q2

# Length is odd
if len(numbers) % 2:
    
    # split point
    half = math.ceil(len(numbers)/2) 
    first = numbers[:half-1]
    second = numbers[half:]
    print(f'min to end Q2 = {first}, end Q2 to max = {second}')
    

    # splits are odd
    if len(first) % 2:
        mid = math.ceil(len(first)/2) - 1
        Qone = first[mid]
        Qthree = second[mid]
        print(f'Q1 = {Qone}, Q3 = {Qthree}')
        IQR = Qthree - Qone
        print(f'IQR = {IQR}')
    
    # splits are even
    else:
        half = int(len(Qone) / 2)
        half1 = half - 1
        Qone_median = (Qone[half] + Qone[half1]) / 2
        Qthree_median = (Qthree[half] + Qthree[half1]) / 2
        print(f'Q1 = {Qone_median}, Q3 = {Qthree_median}')
        IQR = Qthree_median - Qone_median
        print(f'IQR = {IQR}')

# Length is even
else:
    
    # split point
    half = int(len(numbers)/2)
    
    # everything up to Q2
    first = numbers[:half]
    # everything after Q2
    second = numbers[half:]
    print(f'start Q1 to end Q2 {first}, start Q3 to end Q4{second}')

    # splits are odd : [1,2,3]<[3.5]>[4,5,6] from [1,2,3,4,5,6]
    if len(first) % 2:
        
        # mid point 
        med = len(first) // 2
        Qone = first[med]
        Qthree = second[med]
        print(f'Q1 = {Qone}, Q3 = {Qthree}')
        IQR = Qthree - Qone
        print(f'IQR = {IQR}')

    else:
        half = int(len(first) / 2)
        half1 = half - 1
        Qone = (first[half] + first[half1]) / 2
        Qthree = (second[half] + second[half1]) / 2
        print(f'Q1 = {Qone}, Q3 = {Qthree}')
        IQR = Qthree - Qone
        print(f'IQR = {IQR}')
# find median of start to Q2 -> Q1
# find median of Q2 to end -> Q3
# difference between Q3 and Q1