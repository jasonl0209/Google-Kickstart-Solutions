from sys import *
total_cases = int(stdin.readline())
for h in range(total_cases):
    number_of_houses, wallet = map(int, stdin.readline().split())
    list_prices = sorted(list(map(int, stdin.readline().split())))
    total = 0
    i = 0
    for x in range(number_of_houses):
        total+=list_prices[x]
        if total <= wallet:
            i+=1
        else:
            break
    print("Case #"+str(h+1)+":", i)
