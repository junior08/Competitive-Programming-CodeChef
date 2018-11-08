for i in range(int(input())): # number of test cases
    n,m=[int(x) for x in input().split()] # n = rows, m = columns of the chocolate
    if (n*m)%2==0:
        print("Yes") # the person who moves first wins
    else:
        print("No") # otherwise
