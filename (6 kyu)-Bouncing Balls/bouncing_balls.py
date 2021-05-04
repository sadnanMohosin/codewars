def bouncing_ball(h, bounce, window):
    
    count = 1 
    
    if (bounce >= 1) or (bounce <=0) or (h <0) or (window<0) or (window==h):
        return -1
        
    while h > window:
        h *=  bounce 
        if h > window:
            count +=2
                
    return count 
