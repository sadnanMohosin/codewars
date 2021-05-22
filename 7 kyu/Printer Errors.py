def printer_error(s):
    # your code
    
    available = 'abcdefghijklm'
    
    numerator = 0
    denominator = len(s)
    
    for i in s:
        if i not in available:
            numerator +=1
    return "{}/{}".format(numerator,denominator)
