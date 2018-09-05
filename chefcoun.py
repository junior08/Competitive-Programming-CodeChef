for k in range(int(input())):
    n=int(input())
    over=2**32
    ele=(over-1)//n
    print("2",end=' ')
    for i in range(over%n):
        print(ele+1,end=' ')
    for i in range(n-(over%n)-1):
        print(ele,end=' ')
    print() 
