for i in range(int(input())):# test cases
    s = input()
    sm = 0
    for i in s:
        if i in "123456789":
            sm += int(i)
    print(sm)
