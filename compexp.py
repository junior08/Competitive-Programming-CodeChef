for i in range(int(input())):
    n, k = [int(x) for x in input().split()]
    print(2 * (n - ((n - 1) / k)))
