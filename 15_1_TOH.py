# this is program solves the problem of tower of annoy recursiverly
# we will also write a fibonacci program recursively.



#implement a stack class with max API
import collections

class Stack:
    # declare class level variable
    block = collections.namedtuple("block",("value","max"))

    def __init__(self):
        self.actual_stack = [] # this is instance variable.

    # is stack empty
    def is_empty(self):
        return len(self.actual_stack) == 0
    
    # pop element from stack
    def pop_stack(self):
        if self.is_empty():
            raise error("stack is empty")
        else:
            return self.actual_stack.pop()

    # get max
    def get_max(self):
        return self.actual_stack[len(self.actual_stack)-1].max
    

    # insert in stack
    def insert_in(self, k):
        if not (self.is_empty()):
            self.actual_stack.append(
                 self.block(k, max(k, self.get_max()))
                 )
        else:
            self.actual_stack.append(
                    self.block(k,k)
                    )


    def show_stack(self):
        for b in self.actual_stack:
            print(b.value, end=",")
        print("")

    def show_maxes(self):
        for b in self.actual_stack:
            print(b.max, end=",")
        print("") 


# three stack for each tower
s1 =[5,4,3,2,1,0] 
s2 =[]
s3 =[] 




print(s1)
print(s2)
print(s3)

def toh(n,a,c,b):
    if n>0:
        # move disk from a to b using c
        toh(n-1,a,b,c)
        # move one disk from a to c
        #print(a)
        #if len(a)>0:
        x = a.pop()
        c.append(x)
        # move disk from b to c using a
        toh(n-1,b,c,a)
    else:
        return


toh(6,s1,s3,s2)

print("new order")
print(s1)
print(s2)
print(s3)
