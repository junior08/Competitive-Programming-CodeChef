mod = 10 ** 9 + 7
for i in range(int(input())):
    a, b , c = [int(x) for x in input().split()]
    first = min(a, b, c)
    last = max(a, b, c)
    mid = a + b + c - first - last
    print((((first % mod) * ((mid - 1) % mod))%mod * ((last - 2) % mod)) % mod)
