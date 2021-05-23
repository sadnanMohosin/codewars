def make_readable(seconds):
    # Do something
    
    min,sec = divmod(seconds,60)
    hour,min = divmod(min,60)
    return f"{hour:02d}:{min:02d}:{sec:02d}"
