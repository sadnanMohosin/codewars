def accum(s):
    # your code
    
    count = 0
    out = []
    for i in s:
        
        out.append(i.upper() + i.lower()*count)
        
        count +=1
        
    return '-'.join(out)
