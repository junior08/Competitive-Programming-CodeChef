l=[]
c=True
while c==True:
    n=int(input())
    if n==42:
        c=False
    elif n<=99:
        l.append(n)
for i in l:
    print(i)
