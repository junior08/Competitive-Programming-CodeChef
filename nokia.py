#nokia

for i in range(int(input())):
    n, m = [int(x) for x in input().split()]
    mn = [0] * 32 #creating the array for placing the soldiers
    for i in range(1, 32):#coz soldiers can't be at the first or last position
        mn[i] = mn[i//2] + mn[i - i//2 -1] + (i + 1)
    mx = n * (n + 3) // 2
    if m < mn[n]:
        print(-1)
    elif m <= mx:
        print(0)
    else:
        print(m - mx)


