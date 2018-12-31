for i in range(int(input())):
    n = int(input())
    prices = [int(x) for x in input().split()]

    prices.sort(reverse = True)
    ans = 0

    for i in range(n):
        if i % 4 < 2:
            ans += prices[i]

    print(ans)

    
