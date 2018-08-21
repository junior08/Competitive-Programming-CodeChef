for i in range(int(input())):
    n, u, d = [int(x) for x in input().split()]
    ht = [int(x) for x in input().split()]
    chute = 0
    curr = ht[0]
    ans = 1
    for hill in range(1, n):
        if ht[hill] <= (curr + u) and (ht[hill] > curr):
            curr = ht[hill]
            ans += 1
        elif ht[hill] >= (curr - d) and (ht[hill] < curr)a:
            curr = ht[hill]
            ans += 1
        elif ht[hill] == curr:
            ans += 1
        elif ht[hill] < (curr - d) and chute == 0:
            chute = 1
            curr = ht[hill]
            ans += 1
        else:
            break
    print(ans)
