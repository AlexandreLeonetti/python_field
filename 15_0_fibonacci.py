# write a program that calculate all fibonacci numbers
# without cashe (slow)
# then with cashe


cache = {}

def fibo(n):# this function is in the order of n

    if n <= 2:
        return 1
    elif n in cache:
        return cache[n]
    else:
        result = fibo(n-1) + fibo(n-2)
    
    # cache the result before returning it.
    cache[n] = result
    return result



print(fibo(90))



def fi(n): # this function is in the order of 2^n
    if n<=2:
        return 1
    else:
        return fi(n-1) + fi(n-2)


print(fi(35)) # this calculation takes longer time because value is not cashed
