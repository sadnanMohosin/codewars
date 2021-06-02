def positive_sum(arr):
    total = []
    if arr == []:
        return 0
    for i in arr:
        if i <0:
            pass
        else:
            total.append(i)
    return sum(total)
