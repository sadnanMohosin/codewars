def make_readable(seconds):
    # Do something
    
    min,sec = divmod(seconds,60)
    hour,min = divmod(min,60)
    return "{:02}:{:02}:{:02}".format(hour,min,sec)
