for i in range(int(input())):
    n, k = [int(x) for x in input().split()]
    time = [int(x) for x in input().split()]
    profit = [int(c) for c in input().split()]
    mx = -1

    for i in range(n):
        stones = k // time[i]
        profit_total = profit[i] * stones
        if profit_total > mx:
            mx = profit_total
    print(mx)
