for i in range(int(input())):
    n, a, b = [int(c) for c in input().split()]
    impossible = 0
    arr = [abs(int(x)) for x in input().split()]

    if a in arr or -a in arr or b in arr or -b in arr:
        print(1)
        continue

    if a == 0 or b == 0:
        print(2)
        continue
    if a == -b:
        for move1 in arr:
            a_left = abs(a - move1)
            b_left = abs(b - move1)
            if a_left in arr or b_left in arr:
                continue
            else:
                impossible = 1 
                break
        else:
            print(2)
            continue

    print(0)
