# this program takes a int and returns a string
#import strings



def int_to_str(n):
    s = [] 
    while n>0:
        c = n%10
        s.append(chr(ord('0')+c))
        n = n//10
    s.reverse() 
    print("".join(s))
    
    return "".join(s)



int_to_str(123)
