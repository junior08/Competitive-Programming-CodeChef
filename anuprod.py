mod = 10 ** 9 + 7

n = int(input())
a = [int(c) for c in input().split()]
ans = 1
for i in a:
    ans = ((ans % mod) * (i % mod)) % mod
print(ans % mod)
