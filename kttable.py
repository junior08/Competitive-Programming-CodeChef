for i in range(int(input())): # number of test cases
    n=int(input()) # number of students
    l=[int(x) for x in input().split()] # time at which students should finish cooking
    l2=[]
    l2.append(l[0])
    k=0
    for c in range(1,len(l)):
        l2.append(l[c]-l[c-1])
    l3=[int(x) for x in input().split()] # time required for each student to cook
    for i,j in zip(l2,l3):
        if j<=i:
            k+=1
    print(k)
