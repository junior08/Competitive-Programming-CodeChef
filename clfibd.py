for i in range(int(input())):
    s = input().strip()
    if len(set(s)) < 3:
        print("Dynamic")
        continue

    l = []
    hsh = [0 for i in range(26)]
    flag = 0
    for i in s:
        hsh[ord(i) - 97] += 1

    for i in hsh:
        if i:
            l.append(i)
            
    l.sort()
    #print(l)
    n = len(l)

    if n >= 4 and l[3] != l[2] + l[1]:
        l[0], l[1] = l[1], l[0]
        
    flag = 1
    if n >= 3:
        for i in range(2, n):
            if l[i] != l[i - 1] + l[i - 2]:
                flag = 0
                break
    if flag:
        print("Dynamic")
    else:
        print("Not")
