#### Given a string, find out if its characters can be rearranged to form a palindrome.
def palindromeRearranging(inputString):
  '''Returns boolean value for whether or not a string of lowercase letters
    can be rearranged to form a palindrome. noqa.

    Parameters:
      inputString (str) : s string of lowercase letters

    Returns:
      Bool : True/False
  '''
  inp_len = len(inputString)
  
  if inp_len < 1:
    return False

  chr_cnt = {}

  for chr in set(inputString):
    chr_cnt[chr] = inputString.count(chr)


  # Even string length
  if inp_len % 2 == 0:
    
    odd_cnt = 0
    for chr in chr_cnt.keys():
      if chr_cnt[chr] %2 != 0:
        odd_cnt += 1

    if odd_cnt > 0: # in an even length string, one odd character count is disqualifying 
      return False
    
    else:
      return True
  
  # Odd string length
  else: 
    odd_cnt = 0
    for cnt in chr_cnt.values():
      if cnt % 2 != 0:
        odd_cnt +=1

    if odd_cnt > 1: # in an odd length string, more that one odd character is disqualifying
      return False
    
    else:
      return True