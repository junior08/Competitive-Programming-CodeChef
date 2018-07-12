perf = []
def findvalid():

    for i in range(1, 10 ** 5 + 1):
        square = i ** 2
        s = set(str(square))
        for digit in s:
            if digit == '1' or digit == '0' or digit == '4' or digit == '9':
                cool = True
            else:
                cool = False
                break

        if cool:
            perf.append(square)
            
findvalid()

from bisect import bisect_left as bl
for i in range(int(input())):
    allowed = [0, 1, 4 , 9]

    a, b = [int(x) for x in input().split()]
    left = bl(perf, a)
    right = bl(perf, b)
    if perf[right] == b:
        right += 1

    print(right - left)
    

    
