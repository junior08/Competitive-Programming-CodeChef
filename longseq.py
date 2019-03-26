T=int(input())
D=[]
for i in range(0,T):
    D.append(input())
c=0
for i in D:
    c=0
    for j in i:
        if j=='1':
            c=c+1
    if c==(len(i)-1) or c==1:
        print('Yes')
    else:
        print('No')
