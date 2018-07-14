from itertools import combinations as cb
for i in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    l.sort()
    c=0
    maxval=l[-1]+l[-2]
    pairs=(n*(n-1))//2
    for i in cb(l,2):
        if sum(i)>=maxval:
            c+=1
    print(c/pairs)
