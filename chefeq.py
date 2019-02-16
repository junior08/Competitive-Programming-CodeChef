for i in range(int(input())):
    n = int(input())
    coins = [int(x) for x in input().split()]

    hsh = [0 for i in range(10 ** 5 + 1)]
    for i in coins:
        hsh[i] += 1
    print(n - max(hsh))
