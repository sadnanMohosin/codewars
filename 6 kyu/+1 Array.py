def up_array(arr):
    #your code here
    
    if len(arr)<1:
        return None
    for i in arr:
        if i<0 or len(str(i))>1:
            return None
    num_lst = "".join(str(a) for a in arr)
    
    num_lst = int(num_lst)+1
    
    return list(map(int,str(num_lst)))
