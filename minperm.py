for i in range(int(input())):
    n=int(input())
    if n%2==0:
        for i in range(2,n+1,2):
            print(i,end=' ')
            print(i-1,end=' ')
    else:
        for i in range(2,n+1,2):
            print(i,end=' ')
            if i-1==n-2:
                print(n,end=' ')
                print(n-2,end=' ')
            else:
                print(i-1,end=' ')
