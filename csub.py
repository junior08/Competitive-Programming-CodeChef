for i in range(int(input())):
    n = int(input())
    s = input()
    coun = s.count('1')
    print((coun * (coun + 1)) // 2)
