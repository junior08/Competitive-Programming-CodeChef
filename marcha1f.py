from itertools import combinations as cb
for loops in range(int(input())):
    denom=[]
    found=0
    n,m=[int(x) for x in input().split()]
    for i in range(n):
        denom.append(int(input()))
    for k in range(1,n+1):
        for i in cb(denom,k):
            if sum(i)==m:
                found=1
                break
    if found==1:
        print('yes')
    if found==0:
        print('No')
        
            
            
