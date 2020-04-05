class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.data = key 
  
  
# A function to do inorder tree traversal 
def printInorder(root): 
  
    if root: 
  
        
        printInorder(root.left) 
  
         
        print(root.data), 
  
         
        printInorder(root.right) 
  
  
  
# A function to do postorder tree traversal 
def printPostorder(root): 
  
    if root: 
  
         
        printPostorder(root.left) 
  
         
        printPostorder(root.right) 
  
        
        print(root.data), 
  
  
# A function to do preorder tree traversal 
def printPreorder(root): 
  
    if root: 
  
         
        print(root.data), 
  
         
        printPreorder(root.left) 
  
         
        printPreorder(root.right) 
  
  
# Driver code 
root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5)
root.left.right.right = Node(6)
root.right.left = Node(7)
root.right.left.right = Node(8)
root.right.right = Node(9)
print("Preorder traversal of binary tree is")
printPreorder(root) 
  
print("\nInorder traversal of binary tree is")
printInorder(root) 
  
print("\nPostorder traversal of binary tree is")
printPostorder(root) 