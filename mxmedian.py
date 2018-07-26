for i in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    l.sort()
    l2=l[:len(l)//2]
    l1=l[(len(l)//2):]
    print(l1[len(l1)//2])
    for i in range(n):
        print(l2[i],l1[i],end=' ')
    print()
