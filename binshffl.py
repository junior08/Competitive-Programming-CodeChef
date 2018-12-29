for i in range(int(input())):
    a, final = [int(x) for x in input().split()]

    if final - a == 1:
        print(1)
        continue

    b = bin(final)[2:]
    req_one = 
