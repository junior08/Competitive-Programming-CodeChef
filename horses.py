for i in range(int(input())):#for number of test cases
    n = int(input())#accept input
    s = [int(x) for x in input().split()]
    s.sort()
    mn = s[-1]
    
    for i in range(n - 1):
        diff = s[i + 1] - s[i]
        if diff < mn:
            mn = diff
    print(mn)
