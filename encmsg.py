for i in range(int(input())):

    n = int(input())
    w = input()
    word = [i for i in w]
    end = n
    if n % 2:
        end = n - 1

    for i in range(0, end - 1, 2):
        word[i], word[i + 1] = word[i + 1], word[i]
    
    e = 'abcdefghijklmnopqrstuvwxyz'[::-1]

    for i in word:
        print(e[ord(i) - 97], end = '')
    print()
