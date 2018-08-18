#import time
#start = time.clock()
n, q = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
c = 0
hsh = []

h = [0 for i in range(31)]
for i in range(n):
    hsh.append(h[:])
for i in a:
    b = bin(i)
    brev = b[::-1]
    for j in range(31):
        #print(b,len(b))
        if len(b)-2 > j:
            if brev[j] == '1' and c != 0:
                hsh[c][30 - j] = hsh[c-1][30 - j] + 1
            elif brev[j] == '1' and c == 0:
                hsh[c][30 - j] = 1
            elif brev[j] == '0' and c != 0:
                hsh[c][30 - j] = hsh[c-1][30 - j] 
            #print(*hsh[c])
        else:
            hsh[c][30 - j] = hsh[c - 1][30 - j]
        #print(*hsh[c],j)
    #print(hsh[c])
    c += 1

for i in range(q):
    ans =''
    l, r = [int(x) for x in input().split()]
    hshl = hsh[l - 2]
    hshr = hsh[r - 1]
    fin = []
    if l == 1:
        hshl = h
    for i,j in zip(hshr, hshl):
        fin.append(int(i) - int(j))
    for i in fin:
        if i > (r - l +1) // 2 and (r - l + 1)%2 != 0:
            ans += '0'
        elif i >= (r - l +1) // 2 and (r - l + 1)%2 == 0:
            ans += '0'
        else:
            ans += '1'
    print(int(ans, 2))
        
#end = time.clock()
#print(end - start)
