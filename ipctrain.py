import heapq
mx = 99999999

for i in range(int(input())):
    n, d = [int(x) for x in input().split()]
    data, hp = [], []

    for i in range(n):
        days, num_lec, sad = [int(x) for x in input().split()]
        data.append([days, num_lec, sad])
    data = sorted(data)
    data.append([mx, mx, mx])
    person = 0

    for day in range(1, d + 1):
        while data[person][0] <= day:
            
            heapq.heappush(hp, (-data[person][2], data[person][1]))
            person += 1

        if len(hp):
            sad, lec_remaining = heapq.heappop(hp)
            if lec_remaining > 1:
                lec_remaining -= 1
                heapq.heappush(hp, (sad, lec_remaining))

    ans = 0
    for i in hp:
        ans += (-i[0] * i[1])
    print(ans)
