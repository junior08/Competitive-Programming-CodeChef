for i in range(int(input())):
    s = input()
    u, d, prev = 0, 0, ''
    for i in s:
        if i == 'U' and prev == '':
            u += 1
            prev = 'U'
        elif i == 'D' and prev == '':
            d += 1
            prev ='D'
        elif i == 'U' and prev == 'D':
            u += 1
            prev = 'U'
        elif i == 'D' and prev == 'U':
            d += 1
            prev = 'D'
    print(min(u, d))
