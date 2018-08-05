for i in range(int(input())):
    n,k=[int(x) for x in input().split()]
    r=n-k
    if n==k:
        print(1)
    else:
        ans=1
        n=n-1
        k=k-1
        if k>n//2:
            k=n-k
        for i in range(k):
            ans*=n
            ans//=(i+1)
            n-=1
            
        print(int(ans))
