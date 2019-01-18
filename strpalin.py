for i in range(int(input())):
    a = set(input())
    b = set(input())

    if set.intersection(a, b):
        print('Yes')
    else:
        print('No')
    
