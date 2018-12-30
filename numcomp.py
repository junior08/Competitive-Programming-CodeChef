for i in range(int(input())):
    a, b, n = [int(x) for x in input().split()]

    if a == b or (abs(a) == abs(b) and n % 2 == 0):
        print(0)
    elif abs(a) == abs(b) and n % 2:
        if a > b:
            print(1)
        else:
            print(2)
    elif abs(a) > abs(b) and n % 2 == 0:
        print(1)
    elif abs(a) < abs(b) and n % 2 == 0:
        print(2)
    elif  a > b:
        print(1)
    else:
        print(2)
