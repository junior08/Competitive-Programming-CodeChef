for i in range(int(input())):
    s = input()
    if len(s) == len(set(s)):
        print("no")
    else:
        print("yes")
