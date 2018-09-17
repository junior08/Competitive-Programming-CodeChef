for i in range(int(input())):
    s = input()
    n, ans = 0, 0

    for i in range(len(s)):
        if s[i] == '<':
            n += 1
        else:
            n -= 1
            if n == 0 and i == (len(s) - 1):
                ans = len(s)
            elif n == 0:
                ans = i + 1#max(ans, (i + 1))
            elif n <= 0:
                break
    print(ans)
