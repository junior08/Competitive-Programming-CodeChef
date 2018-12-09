from functools import reduce
pref = [0 for i in range(10 ** 5 + 2)]
suff = [0 for i in range(10 ** 5 + 2)]

def gcd(a, b):
    if a == 0:
        return b
    return(gcd(b % a, a))

def pre(a):
    n = len(a)
    pref[0] = a[0]
    suff[n - 1] = a[n - 1]
    for i in range(1, n):
        pref[i] = gcd(pref[i - 1], a[i])
    for i in range(n - 2, -1, -1):
        suff[i] = gcd(suff[i + 1], a[i])

   
for i in range(int(input())):
    n, q = [int(c) for c in input().split()]
    a = [int(x) for x in input().split()]
    pre(a)

    for i in range(q):
        
        l, r = [int(c) for c in input().split()]
        idx_l = l - 1
        idx_r = r - 1
        if idx_l == 0:
            print(suff[idx_r + 1])
        elif idx_r == n - 1:
            print(pref[idx_l - 1])
        else:
            print(gcd(pref[idx_l - 1], suff[idx_r + 1]))
         
