for i in range(int(input())):
    l=[int(x) for x in input().split()]
    s=0
    for j in range(l[0],l[1]+1):
        if str(j)==str(j)[::-1]:
            s+=j
    print(s)
