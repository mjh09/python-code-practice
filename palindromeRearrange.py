# still needs work, permutation function from itertools
# 
def palindromeRearranging(inputString):

  
  def isPali(permutationString):
    '''check is palindrome: even/odds'''
    
    str_len = len(permutationString)
    
    # check for length of zero
    if str_len is 0:
      return False

    # even
    elif str_len % 2 is 0:
      mid = str_len // 2
      split_front = permutationString[:mid]
      split_back = permutationString[mid:]

    # odd
    elif str_len % 2 is not 0:
      mid = str_len // 2
      split_front = permutationString[:mid]
      split_back = permutationString[mid+1:]

    split_back_reverse = list(reversed(split_back))
    split_front_list = list(split_front)

    return split_back_reverse == split_front_list


  # get all possible permutations
  def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

  possible_aggregate = list(permutations(inputString))

  for possible in possible_aggregate:
    possible = "".join(possible)
    if isPali(possible):
      return True
  
  return False