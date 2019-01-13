prime = []
def Sieve(n):#sieve of eratosthenes 
    global prime
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    prime[0], prime[1] = False, False
    
Sieve(1000000)
for i in range(int(input())):#for number of test cases
    l, r = [int(x) for x in input().split()]
    ans = 0
    for i in range(l, r + 1):
        if prime[i]:
            ans += 1
    print(ans)#printing answer
