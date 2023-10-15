# 14.1, binary search tree.

# a tree if is a binary tree if each node corresponds to the following assesment :
# r.left < r < r.right
class TreeNode:
    def __init__(self,data=0,left=None,right=None):
        self.data = data
        self.left = left
        self.right= right

def isBST(r, lowrange = float("-inf"), highrange = float("inf")):
    if not r:
        return True
    elif not lowrange<r.data<highrange :
        return False

    return (isBST(r.left,lowrange,r.data)) and isBST(r.right,r.data,highrange)


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.right = TreeNode(11)


print(isBST(root))
