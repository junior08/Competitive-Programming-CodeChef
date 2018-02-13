for i in range(int(input())):
    l=[int(x) for x in input().split()]
    n=len(l)-1
    l.remove(n)
    print(max(l))
