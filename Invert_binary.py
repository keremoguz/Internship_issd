class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

def invertbinary(root):
    if not root:
        """base case: if there is no node to look for, exit the function"""
        return 
    
    invertbinary(root.left) # traverses left subtree
    invertbinary(root.right) # traverses right subtree
    root.left,root.right = root.right, root.left # swaps the children of the node

def depthfirstValues(root):
    """
    returns the binary tree as a list from left to right
    """
    if root == None:
        return []
    return [root.value,*depthfirstValues(root.left),*depthfirstValues(root.right)]

    
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
k = Node("K")
o = Node("O")
a.left = b
b.left = c
b.right = k
d.left = o
a.right = d
d.right = e

print(depthfirstValues(a))
invertbinary(a)
print(depthfirstValues(a))