def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

prime = [True for i in range(1000001)]
prm = []
n = 1000000
p = 2
while(p ** 2 <= n):
    if prime[p]:
        prm.append(p)
        for i in range(2 * p, n + 1, p):
            prime[i] = False
    p += 1


for i in range(int(input())):
    num = int(input())
    a = [int(x) for x in input().split()]
    gcd_ = a[0]
    flag = 0
    mx = max(a)
    
    for i in a[1:]:
        gcd_ = gcd(i, gcd_)
    if gcd_ == 1:
        print(-1)
        continue

    for i in prm:
        if gcd_ % i == 0:
            gcd_ = i
            break
    
    print(gcd_)


    
    
