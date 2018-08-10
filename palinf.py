for _ in range(int(input())):
    s = list(input())
    n = len(s)
    all9 = True
    if len(set(s))==1 and s[0]=='9':
        nextpal = '1'+'0'*(n-1)+'1'
        print(nextpal)
        continue
    else:
        i, j = 0, n-1
        greater = 0
        while i < j:
            if s[i] < s[j]: greater = 0
            elif s[i] > s[j]: greater = 1
            s[j] = s[i]
            i += 1
            j -= 1
        if i > j:
            i -= 1
            j += 1
        print(greater)
        if not greater:
            while s[i] == '9':
                s[j] = s[i] = '0'
                i -= 1
                j += 1
                
            s[i] = s[j] = str(int(s[i]) + 1)
        print("".join(s))
