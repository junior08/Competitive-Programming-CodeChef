two = [2 ** i for i in range(32)]
from bisect import bisect_left as bl

for i in range(int(input())):
    n = int(input())
    if n == 1:
        print(2)
        continue

    pos = bl(two, n) - 1
    if two[pos + 1] == n:
        print(1)
        continue
    
    sub = two[pos]
    n_rem = n- two[pos]
    pos_rem = bl(two, n_rem) - 1
    
    if two[pos_rem + 1] == n_rem:
        print(0)
        continue
    else:
        if two[pos_rem] == sub:
            print(min(two[pos_rem + 1] - n_rem, two[pos + 1] - n + 1))
        elif two[pos_rem + 1] == sub:
            print(min(n_rem - two[pos_rem], two[pos + 1] - n + 1))
        else:
            print(min(n_rem - two[pos_rem], two[pos_rem + 1] - n_rem, two[pos + 1] - n + 1))
     
