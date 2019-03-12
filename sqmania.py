n = int(input())
side = [int(x) for x in input().split()]
ans = 0

if n == 1:
    print(side[0] * 4)

else:
    dist = [int(x) for x in input().split()]
    for i in range(n):
        if i != n - 1:
            ans += 5 * side[i] + dist[i]
        else:
            ans += 4 * side[i]

    print(ans)

        
