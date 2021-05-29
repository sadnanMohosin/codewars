def iq_test(numbers):
    y = numbers.split()
    evn = 0
    odd = 0
    index = 0
    for i in range(0,len(y)):
        if int(y[i])%2== 0:
            evn +=1
        else:
            odd +=1

    if evn > odd:
        for i in range(0,len(y)):
            if int(y[i])%2 != 0:
                index = i+1
    else:
        for i in range(0,len(y)):
            if int(y[i])%2 == 0:
                index = i+1
    return index

        
