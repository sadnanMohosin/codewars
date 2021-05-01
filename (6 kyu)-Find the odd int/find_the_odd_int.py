def find_it(seq):
    odd = 0
    
    for element in seq:
        #XOR solution 
        odd ^= element
    
    return odd
