for i in range(int(input())):
    s = input()
    e = s.count('E')
    m = s.count('M')
    i = s.count('I')
    t = s.count('T')
    l = s.count('L')

    if e >= 1 and m >= 2 and i >= 2 and t >= 2 and l >= 2 and len(s) == 9:
        print("YES")
    elif e >= 2 and m >= 2 and i >= 2 and t >= 2 and l >= 2 and len(s) > 9:
        print("YES")
    else:
        print("NO")
