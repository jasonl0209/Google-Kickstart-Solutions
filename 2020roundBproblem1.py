from sys import*
num = int(stdin.readline())
for j in range(1, num+1):
    n = int(stdin.readline())
    lst = list(map(int, stdin.readline().split()))
    counter = 0
    for i in range(1, n-1):
        if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
            counter += 1 
    print("Case #"+str(j)+":", counter)
