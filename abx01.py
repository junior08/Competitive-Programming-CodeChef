#sums = ['1', '124875', '9', '147', '157842', '9', '174', '18']
'''def digsum(a, n):
    a %= 9
    #print(a)
    ans = 0
    if a == 0:
        ans = 9
    if n == 1:
        ans = a
    l= sums[a - 1]
    ans = l[n % len(l)]
    print(int(ans))

for i in range(int(input())):
    a, n = [int(x) for x in input().split()]
    digsum(a, n)'''

r = ['1', '124875', '9', '147', '157842', '9', '174', '18']
 
def solve(a, n):
    a %= 9
    if a == 0:
        return 9
    if n == 1:
        return a
    l = r[a - 1]
    return l[n % len(l)]
 
t = int(input())
for _ in range(t):
    print(solve(*map(int, input().split())))

    
