for i in range(int(input())):
    n = int(input())
    mem = [int(x) for x in input().split()]
    ans = mem[0]
    for i in range(n - 1):
        if mem[i + 1] > mem[i]:
            ans += mem[i + 1] - mem[i]
    print(ans)
