for i in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    print(len(l)-max(l))
