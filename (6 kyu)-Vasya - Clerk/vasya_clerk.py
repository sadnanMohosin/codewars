def tickets(people):
    cash = {25:0,50:0,100:0}
    
    for money in people:
        if money == 25:
            cash[25] +=1
            
        elif money ==50:
            if cash[25]==0:
                return "NO"
            cash[50] +=1 #increase count
            cash[25] -=1 #decrease count because of returning exchange
        else:
            cash[100] +=1 #increase count
            if cash[50]>=1 and cash[25] >=1:
                cash[25] -=1 #decrease count because of returning exchange
                cash[50] -=1 #decrease count because of returning exchange
            elif cash[25] >=3:
                cash[25] -=3 #decrease count because of returning exchange
            else:
                return "NO"
            cash[25] 
    return "YES"
