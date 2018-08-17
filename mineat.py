def hour(bn, mid):
    hh = 0
    for i in bn:
        if i < mid:
            hh += 1
        else:
            if i % mid == 0:
                hh += i // mid
            else:
                hh += i // mid + 1
    return hh

for i in range(int(input())):
    n, h = [int(x) for x in input().split()]
    bn = [int(x) for x in input().split()]
    hours = 0

    high = max(bn)
    low = 1
    while low <= high:
        mid = (low + high) // 2
        hours = hour(bn, mid)
        if hours <= h:
            if (mid != 1) and hour(bn, mid - 1) <= h:
                high = mid -1
            else:
                break
        elif hours > h:
            low = mid + 1
    print(mid)
            
