# this program takes a int and returns a string
#import strings



def int_to_str(n):
    s = [] 
    sign = -1 if n<0 else 1
    n = abs(n)
    while n>0:
        c = n%10
        s.append(chr(ord('0')+c))
        n = n//10
    s.reverse() 
    x = "".join(s) if sign>0 else ("-"+"".join(s)) 
    return x 


print(int_to_str(123))

print(int_to_str(-9999))
