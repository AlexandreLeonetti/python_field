# interger add number

# enter string return integer

def str_to_int(s):
    sign = 1
    if s[0]=="-":
        sign = -1
        s = s[1:]
    n = 0
    for c in s:
        #print(c)
        n = n*10 + int(c)
    return n*sign
print(str_to_int("345"))
print(str_to_int("-77345"))
