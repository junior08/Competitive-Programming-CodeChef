prob, sub = [int(x) for x in input().split()]
data, difficulty = [], []
ans = [[] for i in range(prob)]
from bisect import bisect_left as bl

for i in range(prob):
    n = 0
    score = [int(x) for x in input().split()]
    people = [int(x) for x in input().split()]
    new_data = [[x, y] for x, y in zip(score, people)]

    new_data.sort(key = lambda x:x[0])
    for i in range(len(new_data) - 1):
        if new_data[i][1] > new_data[i + 1][1]:
            n += 1
            
    difficulty.append(n)

diff = sorted(difficulty)

for i in range(len(difficulty)):
    lesser = bl(diff, difficulty[i])
    ans[lesser].append(i + 1)
for i in ans:
    if len(i) == 1:
        print(i[0])
    else:
        for j in i:
            print(j)

