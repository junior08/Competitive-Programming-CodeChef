for i in range(int(input())):# Accept input 
    a, b, c = [int(x) for x in input().split()]
    if (a + c) % 2 == 1:
        ans1 = abs(b - ((a + c -1) // 2))
        ans2 = abs(b - ((a + c + 1) // 2))
        print(min(ans1, ans2) + 1)#print answer
    else:
        print(abs(b - (a + c)//2))
