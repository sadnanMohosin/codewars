import string
def to_jaden_case(str):
    # ...
    return string.capwords(str)
  
## or
def to_jaden_case(string):
    
    
    return ' '.join( a.capitalize() for a in string.split())
