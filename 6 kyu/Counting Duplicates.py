def duplicate_count(text):
    
    dic = {}
    for i in text.lower():
        if i not in dic:
            dic[i]=0
        else:
            dic[i]=1
    return sum(dic.values())
