def solve(arr): 
    
    unique_lst = []
    
    for x in arr[::-1]:
        if x not in unique_lst:
            unique_lst.append(x)
    return unique_lst[::-1]
