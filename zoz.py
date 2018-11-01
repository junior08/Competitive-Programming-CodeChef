for i in range(int(input())): # i = number of test cases
    n, k = [int(s) for s in input().split()] # n = size of array A, k = given number
    arr = [int(x) for x in input().split()] # arr = array
    sm = sum(arr) # sum of the elements of the array
    valid = 0

    for i in range(n):
        if arr[i] + k > sm - arr[i]: # checking if the position is valid
            valid += 1
    print(valid) # printing number of valid positions
