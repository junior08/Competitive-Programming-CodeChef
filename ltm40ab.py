from bisect import bisect_left as bl
for i in range(int(input())):
    a, b, c, d = [int(x) for x in input().split()]
    ans = 0

    for i in range(a, b + 1):
        if i < c:
            ans += d - c + 1
        elif i < d:
            ans += d - i

    print(ans)
        
