def duplicate_encode(word):
    #your code here
    word = word.lower()
    brackets = []
    
    for i in word:
        if word.count(i)>1:
            brackets.append(")")
        else:
            brackets.append("(")
    return ''.join(j for j in brackets)
