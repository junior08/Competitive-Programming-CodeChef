for i in range(int(input())):
    l=[]
    l1=[]
    l2=[]
    n,m=[int(x) for x in input().split()]
    for i in range(n):
        l.append(input().replace(" ",""))
    cost1=0
    cost2=0
    s1='RG'
    s2='GR'
    s1=s1*(m//2)+s1[:m%2]
    s2=s2*(m//2)+s2[:m%2]
    for i in range(n//2):
        l1.append(s1)
        l1.append(s2)
        l2.append(s2)
        l2.append(s1)
    if n%2==1:
        l1.append(s1)
        l2.append(s2)
    for i in range(n):
        for j in range(m):
            if l[i][j]!=l1[i][j]:
                if l1[i][j]=='R':
                    cost1+=3
                else:
                    cost1+=5
            if l[i][j]!=l2[i][j]:
                if l2[i][j]=='R':
                    cost2+=3
                else:
                    cost2+=5
    print(min(cost1,cost2))
