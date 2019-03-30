t=int(input())
for i in range(t):
    n=int(input())
    l=[int(x) for x in input().split()]
    if l==l[::-1]:
        s=list(set(l))
        s1=[x for x in range(1,8)]
        if s==s1:
            print("yes")
        else:
            print("no")
    else:
        print("no")
 
