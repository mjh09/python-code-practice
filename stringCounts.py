# from an array of strings, return the strings with the max len

def allLongestStrings(inputArray):
    cnt_dict ={}
    lens =map(lambda x: len(x), inputArray) #  lens for each string
    for cnt in set(list(lens)):
      cnt_dict[cnt] = [] # empty array for each count
  
    for string in inputArray:
        len_cnt = len(string)
        cnt_dict[len_cnt].append(string)


    max_len = max(list(cnt_dict.keys())) 
    max_arr = cnt_dict[max_len]
    

    return max_arr