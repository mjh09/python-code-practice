matr = [[1,0,0,1,1,0],
        [1,0,0,1,0,0],
        [1,0,1,1,0,0],
        [1,1,1,1,0,0]]

region_dict = {}
cnt = 0

for row in matr:
  
  print(f'ROW---{row}')
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
    print(f'curidxs {curidxs} one_segs ---{one_segs}')
    for seg_idx in one_segs:
      
      f=0
      
      for idx in seg_idx:
        
        t=0
        m=0
        
        for reg, reg_idxs in enumerate(curidxs):
          
          if idx in reg_idxs:
            print(f'CONNECTION FOUND --seg_idx={seg_idx}---idx={idx}---reg_idxs={reg_idxs} \n')
            region_dict[reg].extend(seg_idx)
            f=1
            t=1
            m=1
            break
        
        if t is 1:
          print("BREAK HERE")
          break
      
      # no connections found, create new region
      if f is 0:
        print("no connections found, create new region")
        region_dict[cnt] = seg_idx
        cnt+=1
        

  else:
    print(f'one_segs--{one_segs}')
    for idx, val in enumerate(one_segs):
      region_dict[idx] = val
      cnt +=1
    print(f'UPDATED DICT---{region_dict} \n')