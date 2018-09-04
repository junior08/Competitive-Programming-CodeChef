for i in range(int(input())):
    hsh = [0 for i in range(200001)]
    n, k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    arr.sort()
    for i in arr:
        hsh[i] = 1
    if k == 0:
        if arr == range(n):
            print(n)
        else:
            for i in range(len(hsh)):
                if hsh[i] == 0:
                    print(i)
                    break
        continue
    else:
        for i in range(len(hsh)):
            if hsh[i] == 0 and k != 0:
                hsh[i] = 1
                k -= 1
            if k == 0:
                break
        for i in range(len(hsh)):
            if hsh[i] == 0:
                print(i)
                break
