def pref(s):
    ans = 0
    ac, bc = 0, 0
    for i in s: 
        if i == 'a':
            ac += 1
        if i == 'b':
            bc += 1
        if bc < ac:
            ans += 1
    return ans
for i in range(int(input())):
    s, n = input().split()
    n = int(n)
##    print(pref(s * n))
    a = s.count('a')
    b = s.count('b')
    ans1 = pref(s)
    ans2 = pref(s * min(1000, n))
    if pref(s) == 0:
        print(0)
        continue
    if a == b:
        print(ans1 * n)
        continue
    if a > b:
        if n > 1000:
            print(ans2 + (len(s) * (n - 1000)))
        else:
            print(ans2)
    elif b > a:
        print(ans2)
    
        
    
