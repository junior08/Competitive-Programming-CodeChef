for i in range(int(input())):
    s=input()
    st=[]
    c=0
    for i in range(len(s)-1):
        if s[i]+s[i+1] not in st:
            c+=1
            st.append(s[i]+s[i+1])
    print(c)
        
    
