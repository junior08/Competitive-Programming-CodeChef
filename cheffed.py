n = int(input())
def digsum(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

count = 0
for i in range(max(n - 98, 0), n):
    curr = i
    fs = digsum(curr)
    ss = digsum(fs)

    if (curr + fs + ss) == n:
        count += 1

print(count)
