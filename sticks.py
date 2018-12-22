for i in range(int(input())):#for test casss
    n=int(input())#accepting input
    size=[int(x) for x in input().split()]
    s=set(size)
    s=list(s)
    s.sort()
    area=1
    c=0
    for i in s[::-1]:
        if size.count(i)>=2 and c<2:
            if size.count(i)>=4 and c==0:
                c=2
                area=area*i**2
                break
            else:
                c+=1
                area*=i
        if c>2:
            break
    if c==2:
        print(area)
    else:
        print(-1)
