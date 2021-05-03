def count_bits(n):
    
    binary = bin(n)
    
    binary = binary[2:]
    
    bits = 0
    
    for num in binary:
        if num == "1":
            bits +=1 # count the appearances of 1
            
    return bits
