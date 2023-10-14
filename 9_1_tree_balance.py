import collections
# test if a binary tree is balanced

# inorder, preorder, postorder traversal

# create a tree class 
class treenode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right= right


t1 = treenode(0)
t1.left         =     treenode(1)
t1.right        =     treenode(2)
t1.left.left    =     treenode(3)
t1.left.right   =     treenode(4)
t1.right.left   =     treenode(5)
t1.right.right  =     treenode(6)
t1.right.right.right= treenode(11)
t1.right.right.right.right=treenode(12)# adding this line prove result to be False


def show_tree(r):

    #in order display of nodes.
    if r:
        print(r.data)
        show_tree(r.left)
        show_tree(r.right)


show_tree(t1)

def is_balanced(r):
    block = collections.namedtuple("block",("height", "status"))

    def helper(r):
        #in order traversal
        #explore left
        if not r:
            return block(-1,True)
        left = helper(r.left)
        right= helper(r.right)
        #explore right
        #pass the result up

        height = max(left.height, right.height) + 1
        status = abs(left.height - right.height) <= 1
        
        return block(height, status)

    x = helper(r)
    return x.status 



print(is_balanced(t1))





