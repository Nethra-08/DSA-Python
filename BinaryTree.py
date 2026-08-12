class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            
            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            
            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    
    def preorder(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    
    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")



tree = BinaryTree()


n = int(input("Enter the number of books: "))


print("Enter the titles:")

for i in range(n):
    value = input(f"Enter title {i + 1}: ")
    tree.insert(value)


print("\nInorder traversal:")
tree.inorder(tree.root)

print("\nPreorder traversal:")
tree.preorder(tree.root)

print("\nPostorder traversal:")
tree.postorder(tree.root)
