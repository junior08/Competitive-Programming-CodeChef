for i in range(int(input())):
    m, w = [x for x in input().split()]

    if len(m) == len(w) and m == w:
        print("YES")
        continue
    elif len(m) == len(w) and m != w:
        print("NO")
        continue

    if len(m) > len(w):
        mx, mn = m, w
    else:
        mx, mn = w, m
    min_len = len(mn)
    c = 0

    for i in mx:
        if min_len == 0:
            break
        if i == mn[c]:
            min_len -= 1
            c += 1

    if min_len == 0:
        print("YES")
    else:
        print("NO")
            
            
