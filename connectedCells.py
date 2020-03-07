def connectedCell(matrix):
  regions = {}
  last_segs = {}
  cnt=0
  for row in matrix:
    one_idxs = [] # holds concurrent 1 indexs in loop (single list)
    one_seg = [] # holds each segment of 1's from loops (list of lists)
    for idx, val in enumerate(row):
      if val is 1:
        one_idxs.append(idx)
        if idx is len(row)-1: # end of row
          one_seg.append(one_idxs)
        continue
      elif one_idxs:
        one_seg.append(one_idxs)
        one_idxs=[] # reset concurrent
      else:
        continue
    
    # after first regions
    if regions:
      #print(f'NEW ROW---{row} \n')
      new_last_segs = {}
      prev=None
      for seg in one_seg:

        merged = 0
        inc_seg = [i+1 for i in seg] # accounting for diagonals
        dec_seg = [i-1 for i in seg]
        
        for key in list(last_segs.keys()):
          arr = last_segs[key]
          adj_set = set(arr) & set(seg)
          diag1_set = set(arr) & set(inc_seg)
          diag2_set = set(arr) & set(dec_seg)
          
          if merged:
            #print("PREV MERGE")
            if adj_set:
              regions[prev].extend(regions[key])
              del regions[key]
            elif diag1_set:
              regions[prev].extend(regions[key])
              del regions[key]
            elif diag2_set:
              regions[prev].extend(regions[key])
              del regions[key]
            else:
              regions[cnt] = seg
              cnt+=1

          elif adj_set:
            #print(f'ADJ SET')
            regions[key].extend(seg)
            if key is prev:
              new_last_segs[key].extend(seg)
              #print(f"MERGED--{regions} \n")
            else:  
              new_last_segs[key] = seg
              merged, prev = 1 , key
              #print(f"MERGED--{regions} \n")
          elif diag1_set:
            #print("DIAG1 SET")
            regions[key].extend(seg)
            if key is prev:
              new_last_segs[key].extend(seg)
              #print(f"MERGED--{regions} \n")
            else:  
              new_last_segs[key] = seg
              merged, prev = 1 , key
              #print(f"MERGED--{regions} \n")
          elif diag2_set:
            #print("DIAG2 SET")
            regions[key].extend(seg)
            if key is prev:
              new_last_segs[key].extend(seg)
              #print(f"MERGED--{regions} \n")
            else:  
              new_last_segs[key] = seg
              merged, prev = 1 , key
              #print(f"MERGED--{regions} \n")
          else:
            regions[cnt] = seg
            new_last_segs[cnt] = seg
            cnt+=1
      
      last_segs=new_last_segs
      #print(f"UPDATED LAST SEGS{last_segs} \n")
    
    # first regions
    else:
      for idx, arr in enumerate(one_seg):
        regions[idx] = arr
        last_segs[idx] = arr
        cnt+=1
      #print(f'FIRST REGIONS---{regions} \n')
  
  max_len = 0

  for reg in list(regions.values()):
    if len(reg) > max_len:
      max_len = len(reg)
  
  return max_len