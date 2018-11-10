def maxSum(arr, n):
    max = 0
    m = [0 for x in range(n)]
    for i in range(n):
        m[i] = arr[i]
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and m[i] < m[j] + arr[i]:
                m[i] = m[j] + arr[i]

    for i in range(n):
        if max < m[i]:
            max = m[i]
 
    return max
for i in range(int(input())):
    n = int(input())
    wt = [int(c) for c in input().split()]
    print(maxSum(wt, n))
