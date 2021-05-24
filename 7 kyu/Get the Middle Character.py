def get_middle(s):
    #your code here
    
    right ,left = 0, len(s)-1
    mid = (right+left)//2
    
    if len(s)%2==0:
        return "".join(s[mid:mid+2])
    else:
        return "".join(s[mid])
