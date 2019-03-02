for i in range(int(input())):
    n, b = [int(x) for x in input().split()]
    ans = n - (n - 1)// b

    print(ans)
    
