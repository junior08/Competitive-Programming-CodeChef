for i in range(int(input())):
    n, p = input().split()
    n = int(n)
    l = []
    dee, dum = 0, 0
    
    for i in range(n):
        l.append(input())
        
    for i in l:
        if i[0] == '0':
            dee += i.count("0")
        else:
            dum += i.count("1")

    if dee > dum:
        print("Dee")
    elif dee < dum:
        print("Dum")
    elif p == "Dee":
        print("Dum")
    else:
        print("Dee")
