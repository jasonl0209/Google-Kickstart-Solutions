from sys import*
num = int(stdin.readline())
for j in range(1, num+1):
    n, d = map(int, stdin.readline().split())
    lst = list(map(int, stdin.readline().split()))
    lst.reverse()
    for elem in lst:
        d = (d//elem) * elem
    print("Case #"+str(j)+":", d)
