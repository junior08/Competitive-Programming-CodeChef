for i in range(int(input())):
    n, k = [int(x) for x in input().split()]
    s = input()
    
    a = 0
    b = 0
    ahere = 0
  
    for i in s:
        if i == 'a':
            a += 1
        elif i == 'b':
            b += 1
            ahere += a
            
    print((ahere * k) + (((k - 1) * k) // 2) * a * b)
