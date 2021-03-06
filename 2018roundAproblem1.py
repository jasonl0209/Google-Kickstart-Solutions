from sys import *
num = int(stdin.readline())

def fast_exponentiation(base, exp):
    if exp == 0:
        return 1 
    elif exp == 1:
        return base 
    else:
        split = fast_exponentiation(base, exp//2)
        if exp % 2 == 0:
            return split * split
        else:
            return split * split * base
            
for j in range(1, num+1):
    n = input()
    int_n = int(n)
    length = len(n)
    bln_all = True
    for k in range(length):
        if int(n[k]) % 2 == 1:
            bln_all = False
            break 
    first_segment = n[0:k]
    
    if bln_all == False:
        if n[k] == "1" and k == 0:
            upper_bound = 2 * (fast_exponentiation(10, length - 1))
            if n != "1":
                lower_bound = int((length - 1) * "8")
            else:
                lower_bound = 0
            diff = min(upper_bound - int_n, int_n - lower_bound)
                    
        elif n[k] == "9":
            lower_bound = first_segment + ("8" * (length - k))
            diff = int_n - int(lower_bound)
                
        else:
            upper_bound = first_segment + str(int(n[k]) + 1)
            lower_bound = first_segment + str(int(n[k]) - 1)
            for x in range(k+1, length):
                upper_bound += "0"
                lower_bound += "8"
            upper_bound = int(upper_bound)
            lower_bound = int(lower_bound)
            diff = min(upper_bound - int_n, int_n - lower_bound)
            
        print("Case #"+str(j)+":", diff)
        
    else:
        print("Case #"+str(j)+":", 0)
        
    
