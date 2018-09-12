for nums in range(int(input())):
    n, m = [int(x) for x in input().split()]
    l = []
    cy, geno = 0, 0
    for j in range(n):
        lis = [int(x) for x in input().split()]
        l += lis
    l.sort()
    for i in range((n * m) - 1, -1 , -2):
        cy += l[i]
    for i in range((n * m) - 2, -1 , -2):
        geno += l[i]
    if cy > geno:
        print("Cyborg")
    elif cy == geno:
        print("Draw")
    else:
        print("Geno")
