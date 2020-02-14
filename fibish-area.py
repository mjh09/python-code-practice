import sys


arg_check = len(sys.argv)

#exit if args dont match requirements
if arg_check < 2 or arg_check > 2:
    sys.exit('Invalid Input: single arg => INT')




# find the area of exapnding square/polygon, increments one new block for each edge
# fibonacci like
def shapeArea(n):
    # should probably use a cache or lru cache
    # check for the first sequences
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        sys.exit('No')
    
    # if not first sequences, increment newly created by 4
    else:
        total = 1
        new = 0
        
        for i in range(n):
            # skip one since its known
            if i == 1:
                continue
            new += 4
            total += new

        return total


n = int(sys.argv[1])
print(shapeArea(n))


