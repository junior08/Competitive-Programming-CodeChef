for i in range(int(input())):
    n = int(input())
    
    if n == 1:
        print(1)
        continue
    '''ans = [ele for ele in range(1, n)]
    ans.append(n ** 2 - sum(ans) + 1)
    print(*ans)'''
    print(*[2*i - 1 for i in range(1, n + 1)])
