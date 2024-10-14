"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    #Write your code here
    h = height(root) 
    for i in range(1, h+1): 
        printGivenLevel(root, i)  
def printGivenLevel(root , level): 
    if root is None: 
        return
    if level == 1: 
        print("%d" %(root.info),end=' ')
    elif level > 1 : 
        printGivenLevel(root.left , level-1) 
        printGivenLevel(root.right , level-1) 
def height(node): 
    if node is None: 
        return 0 
    else :   
        lheight = height(node.left) 
        rheight = height(node.right) 
        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1
  