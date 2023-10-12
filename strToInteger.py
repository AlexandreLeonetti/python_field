# interger add number

# enter string return integer

def str_to_int(s):
    n = 0
    for c in s:
        print(c)
        n = n*10 + int(c)
    return n
print(str_to_int("345"))
