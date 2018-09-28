##def squares(ln):
##    if ln == 4:
##        return 1
##    elif ln < 4:
##        return 0
##    else:
##        return(squares(ln - 2) + (ln - 2) // 2)
for i in range(int(input())):
    b = int(input())
    if b < 4:
        print(0)
        continue
    n = (b // 2) - 1
    print((n * (n + 1)) // 2)
