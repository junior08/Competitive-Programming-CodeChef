for i in range(int(input())):
    n,d = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    avg = sum(a)//n
    c = -1
    done = 0
    f = 0
    ans = 0
    if sum(a)%n!=0:
        print(-1)
        continue
    for i in a:
        c += 1
        #print(i,c+d,a[c+d])
        if c+d < n:
            if i > avg:
                diff = i-avg
                a[c+d] += diff
                a[c] -= diff
                ans += diff
            elif i < avg:
                diff = avg-i
                a[c] += diff
                a[c+d] -= diff
                ans += diff
        else:
            break
    
    if len(set(a))==1:
        print(int(ans))
    else:
        print(-1)
