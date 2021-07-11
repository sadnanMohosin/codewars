def unique_in_order(iterable):
    new_lst = []
    pre_lst = None
    
    for i in iterable:
        if i != pre_lst:
            new_lst.append(i)
            pre_lst = i
    return new_lst
