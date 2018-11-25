def gcd(a, b):#euclidean gcd
    if a == 0:
        return b
    else:
        return(gcd(b % a, a))

def lcm(a, b):#lcm x gcd = a x b
    return((a * b)/gcd(a, b))

for i in range(int(input())):
    n = int(input())

    a = [int(x) for x in input().split()]

    mn = lcm(a[0], a[1])

    for i in range(n):
        for j in range(1, n):
            if i == j:
                continue

            mn = min(lcm(a[i], a[j]), mn)

    print(int(mn))
