for i in range(int(input())):
    s = input()
    rev = s[:: -1]
    l, l_rev = '', ''
    pos, pos_rev = 0,0

    if s == s[:: -1]:
        print("YES")
        continue

    for i in range(len(s)):
        if s[i] != rev[i]:
            pos = i
            break

    pos_rev = len(s) - pos - 1

    for i in range(len(s)):
        if i == pos:
            l_rev += s[i]
        elif i == pos_rev:
            l += s[i]
        else:
            l += s[i]
            l_rev += s[i]
    if l == l[:: -1] or l_rev == l_rev[:: -1]:
        print("YES")
    else:
        print("NO")
