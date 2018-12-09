import random
for i in range(int(input())):
    a = input()
    n = int(input())
    b = [int(x) for x in input().split()]
    ans = ''.join(random.sample(a, len(a)))
    print(ans)
