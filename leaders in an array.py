for i in range(int(input())):
    n = int(input())

    a = [int(x) for x in input().split()][::-1]
    mx = -1
    ans = []
    
    for i in a:
        if i >= mx:
            ans.append(i)
            mx = i
    print(*ans[::-1])
    
