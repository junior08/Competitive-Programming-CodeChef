for i in range(int(input())):
    n = int(input())
    l = []
    sn,sc = 0,0
    if n == 1:
        l = [int(x) for x in input().split()]
        print(l[0])
        continue
    for i in range(n):
        l = [int(x) for x in input().split()]
        sn += l[0]
        sc += l[1]

print(sn - sc)
    
