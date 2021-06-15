def divisors(integer):
    div = []
    for i in range(2,integer):
        if integer%i==0:
            div.append(i)
    if div == []:
        return "{} is prime".format(integer)
    return div
