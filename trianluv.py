def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    else:
        return gcd(b% a, a)

mod = 10 ** 9 + 7
def ncr(n):
    return ((n % mod) * ((n - 1) % mod) * ((n - 2) % mod) // 6) % mod

for i in range(int(input())):
    x1, y1, x2, y2, x3, y3 = [int(x) for x in input().split()]
    ans = 0
    pts_bw1 = (gcd(abs(y1 - y2), abs(x1 - x2)) - 1) % mod
    pts_bw2 = (gcd(abs(y3 - y2), abs(x3 - x2)) - 1) % mod
    pts_bw3 = (gcd(abs(y1 - y3), abs(x1 - x3)) - 1) % mod

    ans = ncr(pts_bw1 + pts_bw2 +pts_bw3 + 3) - ncr(pts_bw1 + 2) - ncr(pts_bw2 + 2) - ncr(pts_bw3 + 2) 
    print(ans % mod)
