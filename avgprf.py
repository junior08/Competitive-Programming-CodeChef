for i in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    
    hsh = [0 for x in range(2005)]
    for i in a:
        hsh[i + 10 ** 3] += 1

    ans = 0
    for i in range(2002):
        if hsh[i]:
            for j in range(1, 2003):
                if i + 2 * j <= 2004 and hsh[i + (2 * j)] and hsh[i + j]:
                    print(i, j)
                    ans += (hsh[i] * hsh[i + 2*j])
            
    for i in hsh:
        if i >= 2:
            ans += ((i - 1) * i) // 2 
    print(ans)

