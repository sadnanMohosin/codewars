def descending_order(num):
    # Bust a move right here
    
    n_list = list(map(int,str(num)))
    n_list = sorted(n_list,reverse = True)
    
    return int(''.join(str(a) for a in n_list))
