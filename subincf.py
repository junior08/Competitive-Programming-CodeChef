for i in range(int(input())):
    n=int(input())
    c=0
    table=[0 for x in range(n)]
    l=[int(x) for x in input().split()]
    table[0]=1
    for i in range(n-1):
        if l[i+1]>=l[i]:
            table[i+1]=1+table[i]
        else:
            table[i+1]=1
    print(sum(table))
            
