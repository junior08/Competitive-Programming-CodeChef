#I'm sorry, I'm sleepy :(
for i in range(int(input())):
    n = int(input())
    if n >= 33:
        print("Case", i + 1, end = '')
        print(":", 8589934592-1)
        continue
    print("Case", i + 1, end = '')
    print(":",(2 ** n) - 1)
