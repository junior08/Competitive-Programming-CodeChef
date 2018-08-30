for i in range(int(input())):
    n,r=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    high=max(a)+1
    low=0
    c=0
    if r!= a[len(a)-1]:
        print('NO')
    for i in range(n-1):
        if low>=high or a[i]>high or a[i]<low:
            c=1
            print('NO')
            break
        if a[i+1]<a[i]:
            high=a[i]
        else:
            low=a[i]
    if c==0 and r<high and r>low:
        print('YES')
    elif c==0:
        print('NO')
