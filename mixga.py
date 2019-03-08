for i in range(int(input())):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    sm = 0

    for i in range(n):
        if i % 2 == 0:
            if sm < 0:
                sm -= a[i]
            else:
                sm += a[i]
        else:
            if sm < 0:
                sm += a[i]
            else:
                sm -= a[i]

    if abs(sm) >= k:
        print(1)
    else:
        print(2)
