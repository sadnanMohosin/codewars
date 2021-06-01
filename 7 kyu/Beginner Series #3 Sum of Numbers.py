def get_sum(a,b):
    
    add  = 0
    if a == b:
        return a 
    elif a<b:
        for i in range(a,b+1):
            add +=i
        return add
    elif a>b:
        for i in range(b,a+1):
            add +=i
        return add
