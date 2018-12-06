for i in range(int(input())):
    n = int(input())
    s = [int(x) for x in input().split()]
    s.sort()
    mn = max(s)
    
    for i in range(n - 1):
        diff = s[i + 1] - s[i]
        if diff < mn:
            mn = diff
    print(mn)
