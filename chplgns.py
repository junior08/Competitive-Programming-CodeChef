from bisect import bisect_left as bl
def polygonArea(X, Y, n):
    area = 0.0
    j = n - 1
    for i in range(0,n):
        area += (X[j] + X[i]) * (Y[j] - Y[i])
        j = i 

    return int(abs(area / 2.0))
 
for i in range(int(input())):
    area = []
    num_polygons = int(input())
    for i in range(num_polygons):
        vertices = int(input())
        pts = [int(x) for x in input().split()]
        x, y = [], []
        

        for j in range(2 * vertices):
            if j % 2:
                y.append(pts[j])
            else:
                x.append(pts[j])

        area.append(polygonArea(x, y, len(x)))

    area_copy = sorted(area)
    for i in area:
        print(bl(area_copy, i), end = ' ')
    print()
