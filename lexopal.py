for i in range(int(input())):
    s = input()
    l = len(s)
    lis = [i for i in s]
    for i in range(l):
        if lis[i] == '.' and lis[l - i - 1] == '.' and i <= l//2:
            lis[i] = 'a'
            lis[l - i - 1] = 'a'
        elif lis[i] == '.' and lis[l - i - 1] != '.':
            lis[i] = lis[l - i - 1]
        elif lis[i] == '.':
            lis[i] = 'a'
    if lis == lis[::-1]:
        print(*lis, sep = '')
    else:
        print(-1)
