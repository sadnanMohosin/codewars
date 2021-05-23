def create_phone_number(n):
    #your code here
    
    str1 = ''.join(str(e) for e in n)
    
    return "(" + str1[:3]+ ")" + " "+ str1[3:6]+"-"+str1[6:]
  
  ##another interesting solution
  
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
