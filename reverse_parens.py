# take input string and reverse inside parenthesis,
# # staring with the inner most first, inplace 

def reverseInParentheses(inputString):
    exclude = ["","()",")","("]
    
    if inputString in exclude:
        return ""
  
    split = lambda x: [chr for chr in x]

    def map_pairs(string):
        idict = {}

        pos= 0
        for idx, char in enumerate(string):
            pos+=1
            if char == '(':
                idict[idx] ='?'
                cnt=0
                for ndx,chr in enumerate(string[idx+1:]):
                    if chr == '(':
                        cnt+=1
                        continue
            
                    elif chr == ')':
                        if cnt > 0:
                            cnt-=1
                            continue

                        elif cnt == 0:
                            idict[idx] = ndx+pos
                            break
        return idict    

    def min_pair(pdict):
        closep = min(list(pdict.values()))
        openp = 0
        for key in pdict:
            if pdict[key] == closep:
                openp = key
                del pdict[key]
                break
        return pdict, openp, closep

    pair_dict = map_pairs(inputString)
    pairs = []
    while len(pair_dict)> 0:
        pair_dict, openp, closep = min_pair(pair_dict)
        pairs.append([openp,closep])

    for plist in pairs:
        first = inputString[:plist[0]+1]
        last = inputString[plist[1]:]
        mid =inputString[plist[0]+1:plist[1]]
        mid = split(mid)
        mid.reverse()
        sep=''
        mid = sep.join(mid)
        inputString = first+mid+last

    complete=''
    alphabet = 'abcedfghijklmnopqrstuvwxyz'
    for char in inputString:
        if char in alphabet:
            complete = complete + char


    return complete