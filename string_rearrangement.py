def stringsRearrangement(InputArray):
  def perm_recur(a):
    if len(a) == 1:
      return [a]

    perm_l = []
    for el in a:
      flg=1
      remaining = []
      for x in a:
        if x != el:
          remaining.append(x)
          continue
        elif flg < 1:
          remaining.append(x)
        flg-=1
      #remaining = [x for x in a if x != el]
      segs = perm_recur(remaining)

      for seg in segs:
        perm_l.append([el] + seg)

    return perm_l

  def possible(arr):
    fp = 0
    sp = 1
    fpp = 0
    spp = 0

    is_within_one = 2

    while is_within_one:
      try:
        list(arr[fp])
        list(arr[sp])
        try:
          if list(arr)[fp][fpp] != list(arr)[sp][spp]:
            if spp == len(list(arr[sp])) - 1:
              if is_within_one == 1:
                return False
            is_within_one -= 1
                      
                      
        
          fpp += 1
          spp += 1
        except:
          if is_within_one == 2:
            return False
          fp += 1
          sp += 1
          fpp = 0
          spp = 0
          is_within_one = 2
      except:
        
        return True
    
    return False

  perms = perm_recur(InputArray)
  
  for perm in perms:
    
    if possible(perm) == True:
      return True
    
  return False