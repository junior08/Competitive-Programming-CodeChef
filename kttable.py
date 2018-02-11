for i in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    l2=[]
    l2.append(l[0])
    k=0
    for c in range(1,len(l)):
        l2.append(l[c]-l[c-1])
    l3=[int(x) for x in input().split()]
    for i,j in zip(l2,l3):
        if j<=i:
            k+=1
    print(k)
