# given an array of words, format for max length
# increasing space between starting left when next word exceeds
def textJustification(words, l):
  
  #check for total being less than or equal to limit
  total = len(" ".join(words))
  if total < l:
    s = " ".join(words)
    s = s.ljust(l," ")
    return [s]
  if total == l:
    return [" ".join(words)]

    
  final = []
  max_l = l
  idx = 0
  ndx = 1
  s = ""

  #start loop for range of array
  for _ in range(len(words)):
      print('start',f'iter: {_}, idx: {idx}, ndx: {ndx}', '\n')
      
      wlen = len(words[idx])

     
     # catch for end of array
      try:
          nlen = len(words[ndx])
      except IndexError:
        print('break')
        check = s+ words[idx]
        s = check.ljust(l, " ")
        final.append(s)
        return final
      
      
      # check if word lenght is less than limit
      if max_l > wlen:
        s = s + words[idx] + " "
        max_l -= wlen + 1
        print(f'add word -> idx:{idx}, cur_s:{s}', '\n')

        #check if next word will exceed limit
        if max_l < nlen:
          print('exceed \n')
          s = s.rstrip(' ')
          space = l - len(s)
          space_cnt = s.count(' ')
          print(space_cnt)
          # pad tail if single word
          if space_cnt == 0:
            print('here')
            s = s.ljust(l, " ")
            final.append(s)
            max_l = l
            s = ""
            idx += 1
            ndx += 1
            max_l = l
            s = ""
            continue
          
          # distribute spaces starting with left and rotaing
          else:
            new_s = s.split(" ")
            indx = 0
              
            for _ in range(space):
              if indx == len(new_s) - 1:
                indx = 0
              new_s[indx] = new_s[indx] + " "
              indx += 1
              
            s = " ".join(new_s)
            final.append(s)
            print(f'ffull-> s:{s}, len:{len(s)}, {final}', '\n')
            
            idx+=1
            ndx+=1
            max_l = l
            s=""
            continue
          
        idx +=1
        ndx+=1
        continue
      
      
      # check if word lenght will equal limit
      elif max_l == wlen:
        s = s + words[idx]
        final.append(s)
        print(f'efull: s:{s}, len:{len(s)}, {final}', '\n')
        max_l = l
        idx += 1
        ndx += 1
        s = ""
        continue

  return final