for k in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    dp = [1 for _ in range(n)]
##    rang = 0
##    curr = 1
    for i in range(n - 2, -1, -1):
        if a[i] * a[i + 1] < 0:
            dp[i] = dp[i + 1] + 1
    print(*dp)
        
	
