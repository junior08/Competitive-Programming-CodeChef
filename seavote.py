for i in range(int(input())):
    n = int(input())
    b = [int(x) for x in input().split()]

    if sum(b) == 100:
        print("YES")
        continue
    
    c = 0
    s = sum(b) - 100
    for i in b:
        if i != 0:
            c += 1

    if s >= 0 and s < c:
        print("YES")
    else:
        print("NO")
            
