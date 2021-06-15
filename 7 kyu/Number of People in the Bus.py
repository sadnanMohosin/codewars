def number(bus_stops):
    # Good Luck!
    
    last = []
    for num in bus_stops:
        last.append(num[0]-num[1])
    return sum(last)
