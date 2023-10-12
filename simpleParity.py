# simple parity program

def parity(X):
    is_even = False
    while X :
        is_even = (X & 1) ^is_even
        X = X >> 1

    return is_even

print(parity(16))
print(parity(32))


# make a hash table 

hash_table = [ parity(x) for x in range(1<<16)]


