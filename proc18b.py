for i in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]

    a.sort(reverse = True)
    avg = (a[0] + a[1]) / 2
    for i in range(2, n):
        avg = (avg + a[i]) / 2
    print(avg)
        
