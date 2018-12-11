from functools import reduce
def gcd(a, b ):
    if a == 0:
        return b
    return gcd(b % a, a)

for i in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    gc = reduce(gcd, a)
    if gc == 1:
        print(0)
    else:
        print(-1)
    
