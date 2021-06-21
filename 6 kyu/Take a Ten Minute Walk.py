def is_valid_walk(walk):
    #determine if walk is valid
    travel = len(walk)==10
    
    ns = walk.count("n")==walk.count("s")
    ew = walk.count("e")== walk.count("w")
    return ns and ew and travel
