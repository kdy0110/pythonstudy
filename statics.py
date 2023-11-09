def getMode(numlist) :
    num_set = set(numlist)
    num_dict = dict()
    for n in num_set : 
        num_dict[n] = numlist.count(n)


    max_num = max(num_dict.values())
    modes = []
    for k,v in num_dict.items( ) : 
        if v==max_num :
          
            #mode = k
            modes.append(k)
            #break
    return modes
