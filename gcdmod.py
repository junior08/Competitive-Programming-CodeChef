mod = 10**9+7
def factor(n):
    factors = []
    for i in range(1,int(pow(n, 0.5) + 1)):
        if n % i == 0:
            factors.append(i)
            factors.append(n//i)
    return list(set(factors))
for t in range(int(input())):    
    a, b, n = [int(i) for i in input().split()]
    if a == b:
        print((pow(a,n,mod)+pow(b,n,mod))%mod)
        continue
    fac = sorted(factor(abs(a-b)))[::-1]
    for i in fac:
        gcd = (pow(a,n,i)+pow(b,n,i))%i
        if gcd == 0:
            print(i%mod)
            break
