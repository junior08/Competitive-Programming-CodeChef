for i in range(int(input())):
    r, g, b, m = [int(x) for x in input().split()]
    red = [int(c) for c in input().split()]
    gre = [int(x) for x in input().split()]
    bl = [int(x) for x in input().split()]

    rmx = max(red)
    gmx = max(gre)
    bmx = max(bl)
    mx = [rmx, gmx, bmx]
    #mx.sort()
    
    while m != 0:
        mx.sort()
        mx[-1] = mx[-1] // 2
        m -= 1

    print(max(mx))
