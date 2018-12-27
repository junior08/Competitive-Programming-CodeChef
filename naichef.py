for i in range(int(input())):
    n, a, b = [int(values) for values in input().split()]
    nums_on_dice = [int(face) for face in input().split()]
    count_a, count_b = 0, 0
    
    for i in nums_on_dice:
        if i == a:
            count_a += 1
        if i == b:
            count_b += 1

    ans = (count_a * count_b) / (n ** 2)

    print(ans)
