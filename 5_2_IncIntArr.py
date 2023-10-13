# increment an integer of arbitrary size
a = [3,4,6,7,3,5]
b = [1,2,3,8,9,9]
c = [9,9,9,9,9,9]

def inc(n):
    for i in reversed(range(len(n))):
        print(n[i])
        x = n[i]
        if x<9:
            x +=1
            n[i] = x
            return n
        else:
            n[i]=0
    
    # if array is full of 9, 
    n.append(1)
    n.reverse()
    return n 
print(inc(a))
print(inc(b))
print(inc(c))
