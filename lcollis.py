for i in range(int(input())):
    b,g=[int(x) for x in input().split()]
    l=[]
    table=[0 for i in range(g)]
    for i in range(b):
        l.append(input())
    c=0
    csion=0
    for i in range(b):
        for j in range(g):
            if l[i][j]=='1':
                table[j]+=1
        
    for i in table:
        csion+=(i*(i-1))//2
    print(csion)
