for i in range(int(input())):
    n, player = [x for x in input().split()]
    pile = [int(x) for x in input().split()]
    n = int(n)

    if n == 1 and player == "Dee" and (pile[0] % 2 == 0):
        print("Dee")
    else:
        print("Dum")
