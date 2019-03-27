t=int(input())
for i in range(t):
    l=[int(x) for x in input().split()]
    c=0
    if l[0]<l[1]:
        for i in range(1,l[0]+1):
            if l[2]%i==0 and l[2]//i<=l[1]:
                c+=1
        print(c)
    else:
        for i in range(1,l[1]+1):
            if l[2]%i==0 and l[2]//i<=l[0]:
                c+=1
        print(c)
 
