for i in range(int(input())):
    n = int(input())
    w = [int(x) for x in input().split()]

    s = set(w)
    if len(s) == 1:
        print(0)
        continue
    print(sum(w) - (n * min(w)))
