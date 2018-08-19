for i in range(int(input())):
    n = int(input())
    amax = [-1 for x in range(2001)]
    for j in range(n):
        a, b = [int(x) for x in input().split()]
        amax[b] = max(amax[b], a)

    bomb = 0
    mx = -1
    for i in range(2001):
        if mx < amax[i] and amax[i] != -1:
            bomb += 1
            mx = i
    print(bomb)
