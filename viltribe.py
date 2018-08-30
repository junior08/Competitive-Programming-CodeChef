for i in range(int(input())):
    s=input()
    table=[0,0]
    dotcount=acount=bcount=flipa=flipb=count=0
    for i in s:
        if i=='A':
            table[1]=0
            if table[0]==1:
                acount=acount+dotcount+1
                dotcount=0
            else:
                dotcount=0
                acount+=1
                table[0]=1
                continue
        elif i=='B':
            table[0]=0
            if table[1]==1:
                bcount=bcount+dotcount+1
                dotcount=0
            else:
                dotcount=0
                bcount+=1
                table[1]=1
                continue
        elif ((table[0]==1 or table[1]==1) and i=='.') and count!=len(s)-1:
            dotcount+=1
        count+=1
    print(acount,'',bcount)
