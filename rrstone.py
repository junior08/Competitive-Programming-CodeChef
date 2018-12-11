n, k = [int(c) for c in input().split()]
a = [int(c) for c in input().split()]
mn, mx= a[0], a[0]

if k == 0:
    print(*a)

for i in range(n):
    if a[i] > mx:
        mx = a[i]
        pos = i
    if a[i] < mn:
        mn = a[i]
        pos = i

if k % 2:
    for i in a:
        print(mx - i, end = ' ')
    print()

elif k % 2== 0 and k != 0:
    for i in a:
        print(i - mn, end = ' ')
    print()
