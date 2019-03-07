for i in range(int(input())):
    n = int(input())

    while True:
        n += 1
        if str(n).count('3') == 3:
            break

    print(n)
