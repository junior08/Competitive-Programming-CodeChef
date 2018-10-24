for i in range(int(input())):
    w, k = input().split()
    k = int(k)
    ans = 0
    answers = []
    n = len(w)
    
    if n == 1:
        print(0)
        continue

    hsh = [0 for i in range(26)]
    for i in w:
        hsh[ord(i) - 97] += 1

    mn = 100000
    for i in range(1, n):
        ans = 0
        for j in hsh:
            if j > 0:
                if j < i:
                    ans += j
                elif j > i + k:
                    ans += j - (i + k)
        answers.append(ans)
    #print(answers)
    print(min(answers))
            
