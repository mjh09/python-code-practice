# given one increment per loop, determine how many loops
# to maker array inncreasing in order, elements stay in place
def arrayChange(inputArray):
  prev = None
  moves = 0
  for idx, val in enumerate(inputArray):
    if prev:
      print(f'PREV FOUND {prev}, CURRENT {val}')
      if val > prev:
        print('CONTINUE')
        prev = val
        continue
      elif val < prev:
        dif = prev - val +1
        print(f'this dif {dif} THIS PREV,VAL{prev,val}')
        moves += dif
        prev = val+dif
      else:
        dif = 1
        moves += dif
        prev = val + dif
    elif prev== 0:
      print(f'PREV FOUND {prev}, CURRENT {val}')
      if val > prev:
        print('CONTINUE')
        prev = val
        continue
      elif val < prev:
        dif = prev - val +1
        print(f'this dif {dif} THIS PREV,VAL{prev,val}')
        moves += dif
        prev = val+dif
      else:
        dif = 1
        moves += dif
        prev = val + dif
    else:
      print(f'HERE {val}')
      prev = val

  return moves