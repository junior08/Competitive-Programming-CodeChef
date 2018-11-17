s = input()
s = s.rstrip("0")
c = 0
ans = 1
not_done = 1
if len(s) == 0:
    print(0)
    not_done = 0
for i in s:
    if c == 0:
        present = i
        c = 1
    else:
        if present != i:
            ans += 1
            present = i
if not_done:
    print(ans)  
