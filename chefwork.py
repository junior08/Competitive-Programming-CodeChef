n = int(input())
c = [int(x) for x in input().split()]
w = [int(x) for x in input().split()]


min1 = -1
min2 = -1
min3 = -1

for i in range(n):
    if w[i] == 1:
        if min1 == -1 or c[i] < min1:
            min1 = c[i]
    if w[i] == 2:
        if min2 == -1 or c[i] < min2:
            min2 = c[i]   
    if w[i] == 3:
        if min3 == -1 or c[i] < min3:
            min3 = c[i]

if min1 == -1 or min2 == -1:
    print(min3)
elif min3 == -1:
    print(min1 + min2)
else:
    print(min((min1 + min2), min3))
