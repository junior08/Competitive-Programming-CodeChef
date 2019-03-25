n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
m = 0
l.sort()
for i in range(n):
    if l[i] * (n - i) > m:
        m = l[i] * (n - i)
print(m)
            
