prime = [True for i in range(10001)]
p = 2
n = 10000

while(p * p <= n):
    if prime[p] == True:
        for i in range(2 * p, n + 1, p):
            prime[i] = False
    p += 1

prime[0] = False
prime[1] = False
prm = []
for i in range(2,len(prime)):
    if prime[i]:
        prm.append(i)

ans =[]
ans.append(0)
ans.append(0)

for i in range(2,10001):
    an = 0
    for q in prm:
        p =  i - (2 * q)
        if p < 2:
            break
        if prime[p]:
            an += 1
            #print(q, an)
    ans.append(an)


for i in range(int(input())):
    n = int(input())    
    print(ans[n])


        
