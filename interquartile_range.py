import math
### steps
numbers = [1,2,3,4,5,6,7,8,9,10,11,12]

# find median -> Q2
if len(numbers) % 2:
    med = math.ceil(len(numbers)/2)
    #med = numbers[med]
    Qtwo = med 
    Qone = numbers[:med-1]
    Qthree = numbers[med:]
    print(f'Q1 = {Qone}, Q3 = {Qthree}')
    
    if len(Qone) % 2:
        Q_med = math.ceil(len(Qone)/2) - 1
        Qone_median = Qone[Q_med]
        Qthree_median = Qthree[Q_med]
        print(f'Q1 = {Qone_median}, Q3 = {Qthree_median}')
        IQR = Qthree_median - Qone_median
        print(f'IQR = {IQR}')
    
    else:
        half = int(len(Qone) / 2)
        half1 = half - 1
        Qone_median = (Qone[half] + Qone[half1]) / 2
        Qthree_median = (Qthree[half] + Qthree[half1]) / 2
        print(f'Q1 = {Qone_median}, Q3 = {Qthree_median}')
        IQR = Qthree_median - Qone_median
        print(f'IQR = {IQR}')
else:
    half = int(len(numbers)/2)
    first = numbers[:half]
    second = numbers[half:]
    print(first, second)

    if len(first) % 2:
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