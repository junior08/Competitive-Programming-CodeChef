l=[int(x) for x in input().split()] # accept input A and B in list l
x= l[0]-l[1] # difference between A and B
if str(x)[0]!='4':
    print('4'+str(x)[1:]) 
else:
    print('5'+str(x)[1:])
