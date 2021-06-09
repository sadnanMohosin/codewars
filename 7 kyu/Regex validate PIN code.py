def validate_pin(pin):
    #return true or false
    
    return len(pin) in (4,6) and pin.isdigit()
