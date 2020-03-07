matr = [[1,0,0,1,1],
        [1,0,0,1,0],
        [1,0,1,1,0],
        [1,1,1,1,0]]
# matr = [
#         [1,0,1,1,0],
#         [1,0,0,0,0],
#         [1,0,1,1,0]
# ]
def con(matr):
  region_dict = {}
  last_segs = {}
  cnt = 0

  for end, row in enumerate(matr):
    
    #print(f'ROW---{row}')
    one_segs = []
    cur_seg = []
    
    for idx, val in enumerate(row):
    
      if val is 1:
        cur_seg.append(idx)
        if idx is len(row)-1:
          #print(f'END IDX --{idx}')
          one_segs.append(cur_seg)
        continue
      
      elif cur_seg:
        one_segs.append(cur_seg)
        cur_seg=[]
        # cnt+=1
      else:
        continue

    if region_dict:
      
      curidxs = list(region_dict.values())
      lastidxs = list(last_segs.values())
      # print(f'CUR IDXS {curidxs}')
      # print(f"ONE SEGS ---{one_segs}")
      new_last_segs={}
      for seg_idx in one_segs:
        
        f=0
        
        for i, idx in enumerate(seg_idx):
          
          t=0
          m=None
          
          for key, val in last_segs.items():
            
            if idx in val:
              #print(f'CUR IDXS {curidxs}')
              #print(f"ONE SEGS ---{one_segs}")
              #print(f"LAST IDXS --- {lastidxs}")
              #print(f'CONNECTION FOUND --seg_idx={seg_idx}---idx={idx}---key, val={key,val}')
              region_dict[key].extend(seg_idx)
              new_last_segs[key] = seg_idx
              f=1
              t=1
              m=key
              break
          
          if t is 1:
            #print(f'LAST SEGS--{last_segs}')
            #print(f"UPDATED DICT {region_dict}")
            remaining = seg_idx[i+1:]
            #print(f'REMAINING --- {remaining}')
            for r in remaining:
              for rkey, rval in last_segs.items():
                #print(f'K V{rkey,rval}---R{r}')
                if r in rval:
                  #print(f'MERGE SEGS')
                  region_dict[cnt] = region_dict[m] + region_dict[rkey]
                  break

            #print("BREAK HERE \n")
            break
        
        # no connections found, create new region
        if f is 0:
          #print("no connections found, create new region")
          region_dict[cnt] = seg_idx
          new_last_segs[cnt] = seg_idx
          cnt+=1
      
      last_segs = new_last_segs
      #print(f'END NEW LAST SEGS -- {new_last_segs} \n')
      if end is len(matr)-1:
        final = list(region_dict.values())
        fin=0
        for arr in final:
          length = len(arr)
          if length > fin:
            fin = length 
        return fin     
    else:
      #print(f'one_segs--{one_segs}')
      
      for idx, val in enumerate(one_segs):
        region_dict[idx] = val
        last_segs[idx] = val
        cnt +=1