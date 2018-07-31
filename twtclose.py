n,k=[int(x) for x in input().split()]
tweet=[0 for x in range(n)]
for i in range(k):
    state=input().strip()
    if state=='CLOSEALL':
        tweet=[0 for x in range(n)]
    else:
        place=int(state[6:])
        if tweet[place-1]:
            tweet[place-1]=0
        else:
            tweet[place-1]=1
    print(tweet.count(1))
        
    
