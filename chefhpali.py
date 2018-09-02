for i in range(int(input())):
    n,a=[int(x) for x in input().split()]
    alph=''.join(str(chr(i)) for i in range(97,123))
    if a==1:
        print(n,'a'*n)
    elif a>=n and a!=1:
        print(1,alph[:n])
    elif a<n and a>2:
        print(1,alph[:a]*(n//a)+alph[:n%a])
    elif a==2 and n==3:
        print(2,'aab')
    elif a==2 and n==5:
        print(3,'aaabb')
    elif a==2 and n==7:
        print(3,'aaababb')
    elif a==2 and n==8:
        print(3,'aaababbb')
    elif a==2:
        if n%2==0 and n<=6:
            print(n//2,'a'*(n//2)+'b'*(n//2))
        elif n>8:
            s='aababb'
            print(4,s*(n//6)+s[:n-(n//6)*6])
