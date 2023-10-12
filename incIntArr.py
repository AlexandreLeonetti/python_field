# increment an integer of arbitrary size
a = [3,4,6,7,3,5]

def inc(n):
    for i in reversed(range(len(n))):
        print(n[i])
        x = n[i]
        if x<9:
            x +=1
            n[i] = x
            break
        
    return n 
print(inc(a))
