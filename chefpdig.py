for i in range(int(input())):
    s=input()
    l=[0 for x in range(0,10)]
    l1=[]
    for i in range(0,10):
        if str(i) in s and (i<6 or i==9):
            l[i]=1
        elif str(i) in s and i>=6:
            l[i]=s.count(str(i))
    for k in range(6,10):
        for j in range(0,10):
            if l[k]!=0 and l[j]!=0 and k!=j:
                if (k*10+j)>=65 and (k*10+j)<=90:
                    print(chr(k*10+j),end='')
            elif k==j and l[k]>1:
                if k!=9:
                    print(chr(k*10+k),end='')
    print()
