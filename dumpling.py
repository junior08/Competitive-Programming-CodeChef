def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

for i in range(int(input())):
    a, b, c, d, k = [int(x) for x in input().split()]
    g1 = gcd(a, b)
    g2 = gcd(c, d)

    lcm = (g1 * g2) // gcd(g1, g2)
    ans = 2 *  (k // lcm) + 1
    print(ans)
