for i in range(int(input())):#Run for t test cases
    n = int(input()) #Take the input
    a = [int(x) for x in input().split()]#Get the array as input and then
    print((n * (n - 1)) // 2)#print the answer
