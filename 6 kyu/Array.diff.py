def array_diff(a, b):
    unique = []
    
    for i in a:
        if i not in b:
            unique.append(i)
    return unique 
