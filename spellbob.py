for i in range(int(input())):
    front = input()
    back = input()

    lis = [[i, j] for i, j in zip(front, back)]

    if ('o' in lis[0] and 'b' in lis[1] and 'b' in lis[2]) or ('b' in lis[0] and 'o' in lis[1] and 'b' in lis[2]) or ('b' in lis[0] and 'b' in lis[1] and 'o' in lis[2]):
        print('yes')
    else:
        print('no')
