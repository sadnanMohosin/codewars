def vowel_indices(word):
    # your code here
    possition = []
    
    for index,vowel in enumerate(word,start = 1):
        if vowel in 'aeiouyAEIOUY':
              possition.append(index)
        
    return possition
