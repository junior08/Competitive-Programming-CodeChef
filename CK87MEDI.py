for i in range(int(input())):
    n,k=[int(x) for x in input().split()]#Read input
    median=(n+k+1)//2
    l=[int(x) for x in input().split()]
    length=len(l)
    if length>=median:
        l.sort()
        print(l[median-1])
    else:
        print(1000)
