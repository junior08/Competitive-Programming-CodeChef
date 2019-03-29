for i in range(int(input())):
    n=int(input())
    s1=s2=0
    l1=[int(x) for x in input().split()]
    l2=[int(x) for x in input().split()]
    for i in range(n):
        if i%2==0:
            s1+=l1[i]
            s2+=l2[i]
        else:
            s1+=l2[i]
            s2+=l1[i]
    print(min(s1,s2))
            
        
