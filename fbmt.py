for i in range(int(input())):
    n=int(input())
    team1=''
    team2=''
    s1=0
    s2=0
    for i in range(n):
        if i==0:
            s=input()
            team1=s
            s1+=1
        elif i!=0 and team2=='':
            ss=input()
            if ss!=team1:
                team2=ss
                s2+=1
            else:
                s1+=1
        elif team2 !='':
            ss=input()
            if ss== team1:
                s1+=1
            else:
                s2+=1
    if s1>s2:
        print(team1)
    elif s1<s2:
        print(team2)
    else:
        print('Draw')
                    
            
       
        
