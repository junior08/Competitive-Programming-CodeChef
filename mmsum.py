for i in range(int(input())):#for given number of test cases 
    n = int(input())
    a = [int(x) for x in input().split()]#accepting input
    max_all = 0
    max_skip = 0
    flag = 0
    ans = 0
    
    for i in a:
        if i >= 0:
            flag = 1
        max_all, max_skip = max(max_all + i, 0),max(0, max_all, max_skip + i)
        ans = max(ans, max_all, max_skip)
    if flag == 1:
        print(ans)
    else:
        print(max(a))#printing answer
