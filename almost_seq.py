#Given an array, determine if it is in sequence of ascending order
# while having the ability to remove 1 element
#TO-DO: write test cases, recursive implementation,..
#  ..check by removing one every time in loop?...
# altenate solution... effiecency 

def almostIncreasingSequence(sequence):

    def check(new_seq):
        cur = 0
        ndx = 1
        for _ in range(len(new_seq) - 1):
            if new_seq[ndx] <= new_seq[cur]:
                try:
                    if new_seq[cur] >= new_seq[ndx+1]:
                        return cur
                except:
                    pass
                return ndx
            else:
                cur += 1
                ndx += 1
        return True

    val = check(sequence)
    if val is True:
        return True
    
    del sequence[val]

    val = check(sequence)
    if val is True:
        return True

    return False

# test cases
a = [1,2,3,4] # true
b = [1,2,4,3] # True
c = [1,2,5,4,3] # False
d = [1,3,2,1] # False
e= [10,1,2,3,4,5] # True
f = [0,-2,5,6] # True
g = [1,3,2] # True
h=[1,2,1,2] # False
i=[1,2,5,3,5] # True

