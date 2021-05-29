def count(string):
    # The function code should be here
    dict = {}
    
    for char in string:
        key = dict.keys()
        if char in key:
            dict[char] +=1
        else:
            dict[char] =1
            
    return dict
