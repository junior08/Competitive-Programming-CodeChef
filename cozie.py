
n , q = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

cumu = [0 for i in range(n + 1)]
for i in range(1, n + 1):
    if arr[i - 1] in [3,4, 6]:
        cumu[i] +=1
    cumu[i] += cumu[i - 1]

for i in range(q):
    l, r = [int(x) for x in input().split()]
    print(cumu[r] - cumu[l - 1])




    
