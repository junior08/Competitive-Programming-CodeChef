for i in range(int(input())):
    n = int(input())

    skip = [int(x) for x in input().split()]

    visited = [0 for i in range(n)]
    ans = 0

    for i in range(n):
        if visited[i] == 0:
            curr = i
            cycle = [curr]

            while (visited[curr] == 0) or (curr in cycle and visited[curr] < 3):
                visited[curr] += 1
                cycle.append(curr)

                curr = (curr + skip[curr] + 1) % n

    for i in visited:
        if i >= 2:
            ans += 1

    print(ans)
        
