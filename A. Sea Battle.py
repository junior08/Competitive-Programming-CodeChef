w1, h1, w2, h2 = [int(c) for c in input().split()]
ans = (2 + w1) + 2 * h1 + (w1 + 2 - w2) + (h2 - 1) * 2 + (w2 + 2)
print(ans)
