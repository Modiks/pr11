class BinaryTreeNode:
    def __init__(self, data):  
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def insert(self, root, data):
        if root is None:
            return BinaryTreeNode(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    def deleteNode(self, root, data):
        if root is None:
            return root

        if data < root.data:
            root.left = self.deleteNode(root.left, data)
        elif data > root.data:
            root.right = self.deleteNode(root.right, data)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                root.data = self.getMin(root.right).data
                root.right = self.deleteNode(root.right, root.data)  

        return root

    def getMin(self, root):
        if root is None:
            return root

        while root.left is not None:
            root = root.left

        return root
    
    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.data,)
            self.in_order(root.right)

    def pre_order(self, root):
        if root:
            print(root.data,)
            self.pre_order(root.left)
            self.pre_order(root.right)

    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data,)   

if __name__ == "__main__":
    tree = BinaryTree()
    root = None

    elements = [5, 3, 2, 1, 0, 7, 9]
    for value in elements:
        root = tree.insert(root, value)

    
    print("In-order traversal:")
    tree.in_order(root)
    print("\nPre-order traversal:")
    tree.pre_order(root)
    print("\nPost-order traversal:")
    tree.post_order(root)

    
    root = tree.deleteNode(root, 9)
    print("\nIn-order traversal after deleting 9:")
    tree.in_order(root)

    root = tree.insert(root, 8)
    print("\nPost-order traversal after adding 8:")
    tree.post_order(root)