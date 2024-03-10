class tree:
    def __init__(self,centre):
        self.centre=centre
        self.left_side=None
        self.right_side=None

def preorder(root):
    if(root):
        print(root.centre,end=" ")
        preorder(root.left_side)
        preorder(root.right_side)

def postorder(root):
    if(root):
        postorder(root.left_side)
        postorder(root.right_side)
        print(root.centre,end=" ")
        
def inorder(root):
    if(root):
        inorder(root.left_side)
        print(root.centre,end=" ")
        inorder(root.right_side)


root=tree(30)
root.left_side=tree(20)
root.right_side=tree(40)
root.left_side.left_side=tree(15)
root.left_side.right_side=tree(25)

print("Preorder Traversal")
preorder(root)
print("\n")
print("Postorder Traversal")
postorder(root)
print("\n")
print("Inorder")
inorder(root)
