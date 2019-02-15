for i in range(int(input())):
    s = [x for x in input()]
    ln = len(s)
    ans1, ans2 = 0, 0
    
    s1 = '-+' * (len(s) // 2) + '-+' * (len(s) % 2)
    s2 = '+-' * (len(s) // 2) + '+-' * (len(s) % 2)
    
    for i, j, k in zip(s1, s2, s):
        if i != k:
            ans1 += 1
        if j != k:
            ans2 += 1

    print(min(ans1, ans2))
