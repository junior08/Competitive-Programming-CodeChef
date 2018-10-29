for i in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    c= 0

    cnt = a.count(2)
    for i in a:
        if i > 2:
            c += 1 
    print(cnt * c + (c * (c - 1) // 2))
