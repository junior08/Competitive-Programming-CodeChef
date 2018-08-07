import math
for i in range(int(input())):
    n,k,s = [int(x) for x in input().split()]
    if (k*7>n*6 and s>6) or k>n:
        print(-1)
        continue
    print(math.ceil((k*s)/n))
