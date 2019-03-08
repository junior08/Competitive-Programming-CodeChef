for i in range(int(input())):
    n, mn = int(input()), 100000000
    val = [int(x) for x in input().split()]
    val.sort()
    
    for i in range(n - 1):
        mn = min(mn, val[i + 1]- val[i])

    print(mn)
        
