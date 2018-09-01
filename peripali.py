for i in range(int(input())):
    n,p=[int(x) for x in input().split()]
    if p==1 or (n==2 and p==2) or p==2 or n%p!=0:
        print('impossible')
    elif n==p:
        print('a'+'b'*(n-2)+'a')
    else:
        print(('a'+'b'*(p-2)+'a')*(n//p))
