for i in range(int(input())):
    cost = [int(c) for c in input().split()]
    hsh = [0 for _ in range(26)]
    ans = 0
    s = list(set(input()))
    for i in s:
        hsh[ord(i) - 97] = 1
    for i in range(26):
        if not hsh[i]:
            ans += cost[i]
    print(ans)
