for i in range(int(input())):
    n, x, y, fx, fy, bx, by = [int(x) for x in input().split()]
    ans = abs(fx - x) + abs(fy - y)

    if (fx == x and x == bx and (by < max(y , fy) and by > min(y, fy))) or (fy == by and y == by and (bx < max(x , fx) and bx > min(x, fx))):
        ans += 2

    print(ans)
