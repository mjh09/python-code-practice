# return the count of pairs in array with with dif of k
# Lower rumtime complexiy
def pairs(k, arr):
    count = 0
    for idx in range(len(arr) - 1):
        cur_val = arr[idx]
        remaining = arr[idx+1:]
        for ndx in range(len(remaining)):
            nxt_val = remaining[ndx]
            differ = abs(nxt_val - cur_val)
            if differ == k:
                count += 1