n = int(input())#for the given number of test cases
def digsum(n):#find the digit sum
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

count = 0
for i in range(max(n - 98, 0), n):
    curr = i
    fs = digsum(curr)
    ss = digsum(fs)

    if (curr + fs + ss) == n:#necessary condition
        count += 1

print(count)#print the answer
