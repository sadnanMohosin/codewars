def calculate_years(principal, interest, tax, desired):
    years = 0
    
    while not principal>=desired:
        principal = principal+principal*interest*(1-tax)
        years +=1
    return years
