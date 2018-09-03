for i in range(int(input())):
    n, p = [int(x) for x in input().split()]
    ppl = [int(x) for x in input().split()]
    mneasy = p//2
    mxhard = p//10
    easy, hard =0, 0
    for i in ppl:
        if i >= mneasy:
            easy += 1
        elif i<= mxhard:
            hard += 1
    if easy == 1 and hard == 2:
        print("yes")
    else:
        print("no")
