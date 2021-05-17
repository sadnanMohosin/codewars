def largest_pair_sum(numbers): 
    # your code here
    
    
    numbers.sort()
    
    return sum(numbers[-2::])
