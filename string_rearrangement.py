def stringsRearrangement(inputArray):
    fp = 0
    sp = 1
    fpp = 0
    spp = 0

    is_within_one = 2

    while is_within_one:
        try:
            list(inputArray[fp])
            list(inputArray[sp])
      
            try:
                if list(inputArray)[fp][fpp] != list(inputArray)[sp][spp]:
                    
                    if is_within_one == 1: 
                        return False
                    is_within_one -= 1
                    
                    
       
                fpp += 1
                spp += 1
            except:
       
                fp += 1
                sp += 1
                fpp = 0
                spp = 0
                is_within_one = 2
        except:
     
            return True
  
    return False