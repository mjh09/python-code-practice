#codesignale previus
def areSimilar(a, b):
    swap1 = None
    swap2 = None
    for i, k in enumerate(b):
        
        if a[i] == k:
            continue
        
        elif swap1:
            
            if swap2 == k:
                
                if i + 1 == len(b):
                    if k == swap2:
                        if swap1 == a[i]:
                            return True
                        else:
                            return False
                    else:
                        return False

                else:
                    arem = a[i+1:]
                    brem = b[i+1:]
                
                try:
                    for idx, val in enumerate(brem):
                        if arem[idx] == val:
                            continue
                        else:
                            return False
                    return True
                
                except TypeError:
                    if brem == arem:
                        return True
                    else:
                        return False
            else:
                return False
        else:
            swap1 = k
            swap2 = a[i]
    return True