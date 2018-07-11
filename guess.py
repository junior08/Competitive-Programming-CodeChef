def gcd(a, b):
    if a == 0:
        return b
    else:
        return(gcd(b % a, a))   #Using Euclid's GCD algorithm


for i in range(int(input())):
    n, m = [int(x) for x in input().split()] # Getting the input

    if n % 2:
        odd_n = n // 2 + 1
    else:
        odd_n = n // 2

    if m % 2:
        odd_m = m // 2 + 1
    else:
        odd_m = m // 2                       # Finding all odd numbers in the range
        

    total_odd = odd_n * (m - odd_m) + odd_m * (n - odd_n) # as odd + even and even + odd will result in odd

    common = gcd(total_odd, n * m)           # Finds GCD of numertr and denomr and divides them to simplify them

    print(str(total_odd // common)+ '/' + str((n * m) //common)) # Prints the result
    
