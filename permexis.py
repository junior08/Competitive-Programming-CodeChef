for i in range(int(input())):
    n = int(input())
    flag = 1

    a = [int(x) for x in input().split()]
    a.sort()
    for i in range(n - 1):
        if a[i + 1] - a[i] > 1:
            flag = 0
            break

    if flag:
        print('YES')
    else:
        print('NO')
