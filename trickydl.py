two = [2 ** i for i in range(100)]

t = int(input())

for _ in range(t):
    a = int(input())

    mx_d, mx, sm, day = [0] * 4

    for i in range(len(two)):
        if sm + two[i] < ((i + 1) * a):
            sm += two[i]
            mx_d += 1

            if (i + 1) * a - sm > mx:
                mx = ((i + 1) * a) - sm
                day = i + 1
    print(mx_d, day)

    
