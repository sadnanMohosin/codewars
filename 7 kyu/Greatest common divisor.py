def mygcd(x, y):
    H = x if x<y else y
    while H >=1:
        if x%H == 0 and y%H == 0:
            return H
        H -=1
