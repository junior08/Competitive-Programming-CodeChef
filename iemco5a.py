for i in range(int(input())):
    n , k = [int(c) for c in input().split()]
    a = [int(x) for x in input().split()]
    ans = 0
    for i in a:
        if i >= k:
            ans += 1
    print(ans)
