def find_short(s):
    s = s.split()
    return len(min(s,key=len))
