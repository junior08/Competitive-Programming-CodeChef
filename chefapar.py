for i in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    if 0 in l:
        print(l.count(0)*1000+(len(l)-l.index(0))*100)
    else:
        print(0)
