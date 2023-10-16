# in this problem we are given an arrayi with a target number
# and find out if tere are three entries that can reach target.
# brute force is n^3
# we must do better.

# a + b + c = x <=> a+b = c-x
# we can do n^2 by looping through a+b == c-x equation


arr = [11,2,5,7,3]

def sum (arr, t):
    hash = [t-c for c in arr]
    for a in arr:
         for b in arr:
                if a+b == t-c:
                    return (a,b,c)


print(sum(arr,21)) # to be studied more




