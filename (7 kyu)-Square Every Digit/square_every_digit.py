def square_digits(num):
    num = str(num)
    
    add = []
    
    for i in num:
        i = int(i)
        add.append(i*i)
    # Converting integer list to string list and joining the list using join()
    return int("".join(map(str,add)))
    pass
