def largest_pair_sum(numbers): 
    # your code here
    
    
    numbers.sort()
    
    return sum(numbers[-2::])

##
def largest_pair_sum(numbers): 
    # your code here
    return sum(sorted(numbers)[-2:])
