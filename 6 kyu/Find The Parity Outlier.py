def find_outlier(integers):
    even = [i for i in integers if i %2==0]
    odd = [j for j in integers if j%2 !=0]
    
    return even[0] if len(even)==1 else odd[0] 
