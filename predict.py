for i in range(int(input())):
    pa = float(input())
    ans = 0.0

    if pa >= 0.50:
        ans = 10000 + 10000 * (1 - pa) * ((2 * pa) - 1)
        print("%.10f"%(ans))
    else:
        ans = 10000 +10000 * pa * (1 - (2 * pa))
        print("%.10f"%(ans))
