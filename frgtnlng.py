for i in range(int(input())):
    n, k = [int(x) for x in input().split()]
    fl = [x for x in input().split()]
    nl = []
    for i in range(k):
        l = [x for x in input().split()]
        nl += l[1:]
    for i in fl:
        if i in nl:
            print("YES", end = ' ')
        else:
            print("NO", end = ' ')
    print()
