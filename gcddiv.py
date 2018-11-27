def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

for i in range(int(input())):
    n, k = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    gcd_all = nums[0]
    for i in nums[1:]:
        gcd_all = gcd(gcd_all, i)

    if gcd_all <= k: #and gcd_all != 1:
        print("YES")
    else:
        if gcd_all % k == 0 and k != 1:
            print("YES")
        else:
            print("NO")
