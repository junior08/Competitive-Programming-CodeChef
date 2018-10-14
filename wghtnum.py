mod = (10 ** 9) + 7
def fast(l,t):
    if t==0:
        return 1
    elif t==1:
        return l
    else:
        r = fast(l,t//2)
        if t%2==0:
            return ((r%1000000007*r%1000000007)%1000000007)%1000000007
        else:
            return ((r%1000000007*l*r%1000000007)%1000000007)%1000000007

for i in range(int(input())):
    n, w = [int(x) for x in input().split()]
    ans = 0
    middle = fast(10, (n - 2))
    for first in range(1,10):
        for last in range(10):
            if last - first == w:
                #print(last, first)
                ans += 1
    print((ans * middle) % mod)
