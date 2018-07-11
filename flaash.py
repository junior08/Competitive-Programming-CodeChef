l=[]
l.append(0)
l.append(0)
l.append(1)
l.append(1)
n=0
for i in range(4,1000001):
    n=l[i-1]
    if i%2==0:
        n=min(n,l[i//2])
    if i%3==0:
        n=min(n,l[i//3])
    l.append(1+n)
for i in range(int(input())):
    print(l[int(input())])
