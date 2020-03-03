# divide array <s> into len(m) segments
# inc count if sum equals m
def birthday(s, d, m):
  
  # starting indexs for length of segment
  ar_idxs = [i for i in range(m)]

  # increments every element in array
  inc_idxs = lambda x: [i + 1 for i in x]

  # current segment
  cur_seg = [s[i] for i in ar_idxs]
  
  cnt=0

  # run
  while True:
    # do this until exception
    try:
      if sum(cur_seg) == d:
        cnt+=1
        ar_idxs = inc_idxs(ar_idxs)
        cur_seg = [s[i] for i in ar_idxs]
      else:
        ar_idxs = inc_idxs(ar_idxs)
        cur_seg = [s[i] for i in ar_idxs]
    
    # end of possible segments
    except IndexError:
      return cnt

  # will probably never hit ?
  return cnt