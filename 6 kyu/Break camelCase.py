def solution(s):
    
    break_cCase = ''
    for letter in s:
        break_cCase += " " + letter if letter.isupper() else letter
    return break_cCase
