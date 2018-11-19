for i in range(int(input())):
    s = input()
    sm = 0
    for i in s:
        if i in "123456789":
            sm += int(i)
    print(sm)
