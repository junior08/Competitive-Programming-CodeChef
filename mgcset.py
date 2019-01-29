for i in range(int(input())):#for each test case
    n, m = [int(x) for x in input().split()]#accepting input

    a = [int(x) for x in input().split()]
    member = 0

    for i in a:
        if i % m == 0:
            member += 1#counting members

    print((2 ** member) - 1)#printing the answer
