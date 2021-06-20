# Stores the answer
ans = []
 
# A Binary tree node
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None
# A iterative function to do postorder traversal of
# a given binary tree
def postOrderIterative(root):
         
    # Check for empty tree
    if root is None:
        return
 
    stack = []
     
    while(True):
         
        while (root):
            # Push root's right child and then root to stack
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)
 
            # Set root as root's left child
            root = root.left
         
        # Pop an item from stack and set it as root
        root = stack.pop()
 
        # If the popped item has a right child and the
        # right child is not processed yet, then make sure
        # right child is processed before root
        if (root.right is not None and
            peek(stack) == root.right):
            stack.pop() # Remove right child from stack
            stack.append(root) # Push root back to stack
            root = root.right # change root so that the
                            # righ childis processed next
 
        # Else print root's data and set root as None
        else:
            ans.append(root.data)
            root = None
 
        if (len(stack) <= 0):
                break
 
# Driver pogram to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
 
print("Post Order traversal of binary tree is")
postOrderIterative(root)
print(ans)
 