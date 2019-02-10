for i in range(int(input())):#for number of test cases
    n=int(input())
    l=[int(x) for x in input().split()]#accepting input
    print(len(l)-max(l))#printing answer 
