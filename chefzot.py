n = int(input())
a = [int(i) for i in input().split()]
b = []
c = []
for i in a:
    
    if i != 0:
        b.append(i)
    else:
        c.append(len(b))
        b = []
c.append(len(b))
if c!= []:
    print(max(c)) 
else:
    print(0)
