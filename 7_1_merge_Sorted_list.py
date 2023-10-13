# write a program that merges two sorted link lists

class listNode:
    def __init__(self, data=0, nextNode=None):
        self.data = data
        self.nextNode = nextNode





root = listNode(0)
root.nextNode= listNode(1)
root.nextNode.nextNode= listNode(2)
root.nextNode.nextNode.nextNode=listNode(5)


r2 = listNode(3)
r2.nextNode = listNode(4)
r2.nextNode.nextNode = listNode(6)
r2.nextNode.nextNode.nextNode = listNode(8)

def showList(r):
    while r:
         print(r.data, end=" ->")
         r= r.nextNode




def merge(l1, l2):
    start = current = listNode(0)

    while l1 and l2:
        if l1.data<l2.data:
            current.nextNode = l1
            l1=l1.nextNode
        else:
            current.nextNode = l2
            l2=l2.nextNode
        current=current.nextNode
    # add all remaining nodes if remaining list exist.
    current.nextNode=l1 or l2

    return start.nextNode 



x = merge(r2,root)
showList(x)

