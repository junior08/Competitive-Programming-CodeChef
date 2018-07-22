for i in range(int(input())):
    n,q=[int(x) for x in input().split()]
    d=[int(x) for x in input().split()]
    x=[int(x) for x in input().split()]
    mul=1
    for i in d:
        mul*=i
    for j in x:
        print(j//mul,end=' ')
    print()
