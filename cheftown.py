n, w = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

sm, sqrsm, ans = 0, 0, 0
b = (w * (w - 1)) // 2
a = (w * (w-1) * (2 * w - 1)) // 6

for i in range(w):
    sm += nums[i]
    sqrsm += nums[i] ** 2

if (sm - b) % w == 0:
    x = (sm - b) // w
    if sqrsm ==  (w * x * x + a + 2 * x * b):
        ans += 1

for i in range(w, n):
    sm += nums[i] - nums[i - w]
    sqrsm += (nums[i] ** 2) - (nums[i - w] ** 2)
    if (sm - b) % w == 0:
        x = (sm - b) // w
        if sqrsm == (w*x*x + a + 2*x*b):
            ans += 1
print(ans)
