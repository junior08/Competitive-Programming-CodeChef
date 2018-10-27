def main():
    prime = [True for i in range(1000001)]
    p = 2
    prm = []
    while (p * p <= 1000001): 
        if (prime[p] == True): 
            prm.append(p)
            for i in range(p * 2, 10 ** 6 +1, p):
                prime[i] = False
        p += 1
        
    c = 1
    pp = prm[::-1]
    prime[0] = prime[1] = False
    while c:
        n = int(input())
        if n == 0:
            c = 0
            continue
        cbrt = int(n ** (1 / 3))
        sqrt = int(n ** (1 / 2))
        flag = 1
        for i in pp:
            if flag:
                for j in pp:
                    if i <= (cbrt  +1) and j<= (sqrt + 1) and (n - i ** 3 - j ** 2) > 0 and prime[n - i ** 3 - j ** 2]:
                        print(n - i ** 3 - j ** 2, j, i)
                        flag = 0
                        break
            else:
                break
        if flag:
            print(0, 0 ,0)
        
main()
