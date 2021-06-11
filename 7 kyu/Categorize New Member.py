def open_or_senior(data):
    return ["Senior" if char[0]>=55 and char[1]>7 else "Open" for char in data]
