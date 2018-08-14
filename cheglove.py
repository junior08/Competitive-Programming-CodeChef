for i in range(int(input())):
    n = int(input())
    finger =[int(x) for x in input().split()]
    glove = [int(x) for x in input().split()]
    front = "yes"
    back = "yes"
    for i,j in zip(finger,glove):
        if i > j:
            front = "no"
    for i,j in zip(finger,glove[::-1]):
        if i > j:
            back = "no"
    if front == "yes" and back == "yes":
        print("both")
    elif front == "yes":
        print("front")
    elif back == "yes":
        print("back")
    else:
        print("none")
             
             
