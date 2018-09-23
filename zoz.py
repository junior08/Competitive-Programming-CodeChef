for i in range(int(input())):
    n, k = [int(s) for s in input().split()]
    arr = [int(x) for x in input().split()]
    sm = sum(arr)
    valid = 0

    for i in range(n):
        if arr[i] + k > sm - arr[i]:
            valid += 1
    print(valid)
