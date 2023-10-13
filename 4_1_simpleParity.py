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
par = hash_table
def word_parity(Z):
    # 64 = 16*4
    # let's break the word into two parts.
    # and sum the parities
    MASK = 0xFFFF 
    part1 = Z & MASK
    part2 = (Z >> 16) & MASK
    part3 = (Z >> 32) & MASK
    part4 = (Z >> 48)

    return par[part1]^par[part2]^par[part3]^par[part4]



print(word_parity((1 << 63) + 1))
