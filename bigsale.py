for i in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(n):
        prc, qty, x = [int(x) for x in input().split()]
        org = prc
        final = 0
        prc = prc+(prc*x)/100
        final = prc - (prc*x)/100
        final = (org-final)*qty
        ans +=final
    print(ans)
