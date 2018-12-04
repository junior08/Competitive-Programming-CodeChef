import math
n = int(input())
smx, smy = 0, 0
pts, lis = [], []
for j in range(n):
    x, y, side = [int(c) for c in input().split()]
    pts.append([x, y])
    smx += x
    smy += y
print(n)
for i in range(n):
    xdiff = n * pts[i][0] - smx
    ydiff = n * pts[i][1] - smy
    angle = math.atan2(ydiff, xdiff)
    lis.append([angle, i])

lis.sort()
for i in range(n):
    pos = lis[i][1]
    print(*pts[pos])
