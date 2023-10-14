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



s1 = Stack()

s1.insert_in(2)
s1.insert_in(5)
s1.insert_in(1)
s1.insert_in(-333)
s1.insert_in(992)

s1.show_stack()
s1.pop_stack()

s1.show_stack()
