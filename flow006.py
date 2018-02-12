t=int(input())
for i in range(t):
    n=int(input())
    sum=0
    while n>0:
        sum+=n%10
        n=n//10
    print(sum)
