coi={0:0,1:1,2:2,3:3}
def coin(n):
    if n in coi:
        return coi[n]
    else:
        coi[n]=max(n,coin(n//2)+coin(n//3)+coin(n//4))
        return coi[n]
while(1):
    try:
        print(coin(int(input())))
    except:
        break
