
for i in range(int(input())):#run for test cases 
    n,k,b = [int(x) for x in input().split()]
    l = [int(x) for x in input().split()]
    l.sort()
    #now = k*l[0]+b
    count = 1
    prev = 0
    for i in range(1,n):
        if l[i] >= k*l[prev]+b:
            count += 1
            prev = i
    print(count)
