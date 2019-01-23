for i in range(int(input())):
    n, m = [int(x) for x in input().split()]

    a = [int(x) for x in input().split()]
    member = 0

    for i in a:
        if i % m == 0:
            member += 1

    print((2 ** member) - 1)
