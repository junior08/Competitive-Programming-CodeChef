for i in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a.sort()
    b.sort()
    asum = sum(a) - a[-1]
    bsum = sum(b) - b[-1]
    if asum > bsum:
        print("Bob")
    elif asum < bsum:
        print("Alice")
    else:
        print("Draw")
