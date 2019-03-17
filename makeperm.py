for i in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0

    hsh = [0 for i in range(n + 5)]

    for i in a:
        if i <= n + 1:
            hsh[i] = 1

    for i in range(1, n + 1):
        if hsh[i] == 0:
            ans += 1

    print(ans)
