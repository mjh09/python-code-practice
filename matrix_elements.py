# find sum of ele's except for eles below 0 in mat

def matrixElementsSum(matrix):
    idxs = []
    total = []
    for row in range(len(matrix)):
        cur_row = matrix[row]
        copy_row = cur_row
        for idx in idxs: # change last rows 0 idxs to zero
            copy_row[idx] = 0
        row_sum = sum(copy_row)
        idxs = [i for i, e in enumerate(cur_row) if e  == 0] # idx of 0's
        total.append(row_sum)
    return sum(total)