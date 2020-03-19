def adjacentElementsProduct(inputArray):
    idx = 0
    ndx = 1
    sums = {}
    for i in range(len(inputArray)):
        sum_of_two = inputArray[idx] * inputArray[ndx]
        sums[sum_of_two] = [inputArray[idx], inputArray[ndx]]
        idx += 1
        ndx += 1

        if ndx == len(inputArray):
            return max(list(sums.keys()))