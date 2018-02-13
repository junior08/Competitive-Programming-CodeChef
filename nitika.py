for i in range(int(input())):
    l=[x for x in input().split()]
    j=0
    while j!=len(l)-1:
        print(l[j][0].upper()+".","",end="")
        j=j+1
    print(l[j][0].upper()+l[j][1:].lower())
        
