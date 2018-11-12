from bisect import bisect_left as bl
def gcd(a, b):
    if a == 0:
        return b
    else:
        return(gcd(b%a, a))
    
n , q, k = [int(x) for x in  input().split()]
a = []
pref = []
seg = []
val = 0

for i in range(n):
    l, r = [int(c) for c in input().split()]
    seg.append([l , r])
    p = (r - l) // k + 1
    if pref != []:  
        pref.append(pref[i - 1] + p)
    else:
        pref.append(p)

for i in range(q):
    p = int(input())
    segn = bl(pref, p)
    l = seg[segn][0]
    #print(l)
    if segn > 0:
        val += l + (p - pref[segn - 1] - 1) * k
    else:
        val += l + (p - 1) * k
    #print("vallues is", val)

gc = gcd(val, q)
print(str(val // gc)+"/"+str( q // gc))
