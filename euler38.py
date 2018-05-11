''' Euler 38 '''

digits = '123456789'
num = 1
condition = 1
maxpan = 0
while num < 9877:
    check = 0
    pandig = ''
    n = 1
    while len(pandig) < 9:
        pandig += str(n*num)
        print(pandig)
        n += 1

    if len(pandig) == 9:
        check = 1
        for i in digits:
            if i not in pandig:
                check = 0

    if check and (maxpan < int(pandig)):
        maxpan = int(pandig)

    num += 1

print(maxpan)
