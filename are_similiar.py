# all tests passed
def areSimilar(a, b):
    swapB = None
    swapA = None

    for i, b_val in enumerate(b):
        
        # same val
        if a[i] == b_val:
            
            # end of array
            if i + 1 == len(b):
                
                # previous mismatch
                if swapB:
                    return False
                
                else:
                    return True
            
            else:
                continue
        
        # mismatch happened
        elif swapB:
            
            # end of array
            if i + 1 == len(b):
                
                if swapA == b_val:
                    
                    if swapB == a[i]:
                        return True
                    else:
                        return False
                
                else:
                    return False
                
            # one remaining in array
            elif i + 2 == len(b):
                
                if b[-1] == a[-1]:
                    
                    if swapA == b_val:
                        
                        if swapB == a[i]:
                            return True
                        else:
                            return False
                    else:
                        return False
                
                else:
                    return False
            
            # more than one remaining
            else:
                arem = a[i + 1:]
                brem = b[i + 1:]
                    
                
                for idx, val in enumerate(brem):
                    
                    if arem[idx] == val:
                        continue

                    else:
                        return False
                if swapA == b_val:
                  if swapB == a[i]:
                    return True
                  else:
                    return False
                else:
                  return False
                

        # neither same val or previous mismatch and end of list
        elif i + 1 == len(b):
            return False
        
        # first mismatch, more unchecked array
        else:
            swapB = b_val
            swapA = a[i]


##################################################
# #codesignale previus
# def areSimilar(a, b):
#     swap1 = None
#     swap2 = None
#     for i, k in enumerate(b):
        
#         if a[i] == k:
#             continue
        
#         elif swap1:
            
#             if swap2 == k:
                
#                 if i + 1 == len(b):
#                     if k == swap2:
#                         if swap1 == a[i]:
#                             return True
#                         else:
#                             return False
#                     else:
#                         return False

#                 else:
#                     arem = a[i+1:]
#                     brem = b[i+1:]
                
#                 try:
#                     for idx, val in enumerate(brem):
#                         if arem[idx] == val:
#                             continue
#                         else:
#                             return False
#                     return True
                
#                 except TypeError:
#                     if brem == arem:
#                         return True
#                     else:
#                         return False
#             else:
#                 return False
#         else:
#             swap1 = k
#             swap2 = a[i]
#     return True



#     #############################################
#     #Dif version, less test cases passed
#     def areSimilar(a, b):
#     swapB = None
#     swapA = None

#     for i, b_val in enumerate(b):
        
#         # same val
#         if a[i] == b_val:
#             if i + 1 == len(b):
#                 if swapB:
#                     return False
#                 else:
#                     return True
#             continue
        
#         # mismatch happened
#         elif swapB:
            
#             if swapA == b_val:
                
#                 # other pair
#                 if swapB == a[i]:
                  
#                   # end of list
#                   if i + 1 == len(b):
#                       return True
                  
#                   # one remaining
#                   elif i + 2 == len(b):
#                     if b[-1] == a[-1]:
#                       return True
#                     else:  
#                       return False
                
#                   else:
#                     arem = a[i+1:]
#                     brem = b[i+1:]
#                     print(arem,brem)
#                     for idx, val in enumerate(brem):
#                         if arem[idx] == val:
#                             continue
#                         else:
#                           return False
#                     return True
#                 else:
#                   return False
#             else:
#               return False
#         elif i + 1 == len(b):
#             return False
#         else:
#             swapB = b_val
#             swapA = a[i]
#     return True