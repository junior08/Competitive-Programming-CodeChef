for i in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    mn = min(b) - 1
    mx = 9999999999999
    all_pair = []

    for i in range(n):
        a[i] %= b[i]
        all_pair.append([a[i], b[i]])
        mx = min(mx, all_pair[i][1] - 1)

    all_pair.sort()
    left = [0 for x in range(n + 1)]
    right = left[:]

    for i in range(n):
        left[i + 1] = left[i] + all_pair[i][0]

    for i in range(n - 1, -1, -1):
        right[i] = right[i + 1] + (all_pair[i][1] - all_pair[i][0])% all_pair[i][1]
##    right = left[::-1]
    ans = right[0]
##    print('r', right)
##    print('l', left)
    for i in range(n):
        if all_pair[i][0] <= mx:
##            print(all_pair[i][0] - left[i + 1] + right[i + 1])
            ans = min(ans, (n *all_pair[i][0]) - left[i + 1] + right[i + 1])

    print(ans)
