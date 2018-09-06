def main():
    n, cuts = [int(x) for x in input().split()]
    allowed = [int(x) for x in input().split()]
    flag = 0
    ans = 0
     
    allowed.sort()
    for i in allowed[::-1]:
        if cuts > i:
            ans += (1 / 2) * (i ** 2 + i + 2)
            #print(ans)
            cuts -= i
        elif cuts == 0:
            ans += 1
            
        else:
            ans += (1 / 2) * (cuts ** 2 + cuts + 2)
            cuts = 0
    print(int(ans))
main()
