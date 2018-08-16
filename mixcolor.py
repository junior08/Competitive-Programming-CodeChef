for i in range(int(input())):
    n = int(input())
    c = [int(x) for x in input().split()]
 
    s = set(c)
    if len(s)==n:
        print(0)
        continue
    else:
        print(n-len(s)) 
