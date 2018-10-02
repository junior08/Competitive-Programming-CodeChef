def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

for i in range(int(input())):
    a, b = [int(x) for x in input().split()]
    print(2* gcd(a, b))
