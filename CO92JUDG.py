for i in range(int(input())): # number of test cases
    n = int(input()) # number of races
    a = [int(x) for x in input().split()] # time taken by alice to finish each x-th race
    b = [int(x) for x in input().split()] # time taken by bob to finish each x-th race
    a.sort()
    b.sort()
    asum = sum(a) - a[-1]
    bsum = sum(b) - b[-1]
    if asum > bsum:
        print("Bob") # Bob wins
    elif asum < bsum:
        print("Alice") # Alice wins
    else:
        print("Draw") # draw
