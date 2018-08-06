#Sorry for WA, I am sleepy 
for i in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    if sum(l)%2==0 and sum(l)!=1:
        print(1)
    elif len(l)==1:
        print(1)
    else:
        print(2)
