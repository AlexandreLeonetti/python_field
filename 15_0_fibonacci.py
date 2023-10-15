# write a program that calculate all fibonacci numbers
# without cashe (slow)
# then with cashe


cache = {}

def fibo(n):

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
