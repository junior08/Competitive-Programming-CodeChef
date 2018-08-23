for i in range(int(input())):
    n, c = [int(x) for x in input().split()]
    candies = [int(x) for x in input().split()]
    if c >= sum(candies):
        print("Yes")
    else:
        print("No")
