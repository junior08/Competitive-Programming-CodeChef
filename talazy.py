for i in range(int(input())):
    n, b, m = [int(x) for x in input().split()]
    solve_time, break_time = 0, 0

    while n > 0:
        if n % 2:
            solve_time += ((n + 1) // 2) * m
            n -= (n + 1) // 2
            

        else:
            solve_time += (n // 2) * m
            n //= 2
        if n:
            break_time += b
        m *= 2

    print(solve_time + break_time)
        
