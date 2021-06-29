def max_multiple(divisor, bound):
    num = []
    
    for i in range(1,bound+1):
        if i % divisor==0:
            num.append(i)
    return max(num)
