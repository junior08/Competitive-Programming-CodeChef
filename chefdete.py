n = int(input())
l = [int(x) for x in input().split()]
s=set(l)
for i in range(1,n+1):
    if i not in s and l[i-1]!=0:
        print(i,end=' ')
