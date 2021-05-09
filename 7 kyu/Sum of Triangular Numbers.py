def sum_triangular_numbers(n):
    #your code here
    sum = 0 
    
    for num in range(1,n+1):
        
        sum += num*(num+1)/2
        
    return sum 
  
  ## formula of finding Sum of Triangular Numbers = (i*(i+1))/2
