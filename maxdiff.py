for i in range(int(input())):
    n,k=[int(x) for x in input().split()]
    wt=[int(x) for x in input().split()]

    wt.sort()

    kid=min(sum(wt[:k]),sum(wt[:n-k]))
    dad=sum(wt)-kid
    print(dad-kid)
