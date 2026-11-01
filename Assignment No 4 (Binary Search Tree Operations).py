import copy
from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(root, key):
            if root is None:
                return Node(key)
            if key < root.key:
                root.left = _insert(root.left, key)
            elif key > root.key:
                root.right = _insert(root.right, key)
            else:
                print(f"Duplicate entry '{key}' not inserted.")
            return root
        self.root = _insert(self.root, key)

    def delete(self, key):
        def _min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(root, key):
            if not root:
                return root
            if key < root.key:
                root.left = _delete(root.left, key)
            elif key > root.key:
                root.right = _delete(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                temp = _min_value_node(root.right)
                root.key = temp.key
                root.right = _delete(root.right, temp.key)
            return root

        self.root = _delete(self.root, key)

    def search(self, key):
        def _search(root, key):
            if not root or root.key == key:
                return root
            if key < root.key:
                return _search(root.left, key)
            else:
                return _search(root.right, key)
        return _search(self.root, key)

    def inorder(self):
        result = []
        def _inorder(root):
            if root:
                _inorder(root.left)
                result.append(root.key)
                _inorder(root.right)
        _inorder(self.root)
        return result

    def preorder(self):
        result = []
        def _preorder(root):
            if root:
                result.append(root.key)
                _preorder(root.left)
                _preorder(root.right)
        _preorder(self.root)
        return result

    def postorder(self):
        result = []
        def _postorder(root):
            if root:
                _postorder(root.left)
                _postorder(root.right)
                result.append(root.key)
        _postorder(self.root)
        return result

    def depth(self):
        def _depth(node):
            if not node:
                return 0
            return 1 + max(_depth(node.left), _depth(node.right))
        return _depth(self.root)

    def mirror(self):
        def _mirror(node):
            if node:
                node.left, node.right = _mirror(node.right), _mirror(node.left)
            return node
        self.root = _mirror(self.root)
        print("Tree mirrored successfully.")

    def copy(self):
        return copy.deepcopy(self)

    def display_parents(self):
        result = []
        def _display(root):
            if root:
                children = []
                if root.left:
                    children.append(root.left.key)
                if root.right:
                    children.append(root.right.key)
                if children:
                    result.append((root.key, children))
                _display(root.left)
                _display(root.right)
        _display(self.root)
        return result

    def display_leaves(self):
        leaves = []
        def _leaves(node):
            if node:
                if not node.left and not node.right:
                    leaves.append(node.key)
                _leaves(node.left)
                _leaves(node.right)
        _leaves(self.root)
        return leaves

    def level_order(self):
        if not self.root:
            return []
        result = []
        queue = deque([self.root])
        while queue:
            level_size = len(queue)
            level_nodes = []
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.key)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_nodes)
        return result

# Menu-Driven Interface
def main():
    bst = BST()
    copied_bst = None

    while True:
        print("\n--- Binary Search Tree Operations Menu ---")
        print("1. Insert Node")
        print("2. Delete Node")
        print("3. Search for Node")
        print("4. Display Traversals")
        print("5. Display Tree Depth")
        print("6. Mirror Image of Tree")
        print("7. Copy Tree")
        print("8. Display Parent Nodes with Children")
        print("9. Display Leaf Nodes")
        print("10. Display Tree Level-wise")
        print("11. Exit")
        
        choice = input("Enter your choice (1-11): ")

        if choice == '1':
            value = int(input("Enter value to insert: "))
            bst.insert(value)
        elif choice == '2':
            value = int(input("Enter value to delete: "))
            bst.delete(value)
        elif choice == '3':
            value = int(input("Enter value to search: "))
            node = bst.search(value)
            if node:
                print(f"Value {value} found in the tree.")
            else:
                print(f"Value {value} not found.")
        elif choice == '4':
            print("Inorder:", bst.inorder())
            print("Preorder:", bst.preorder())
            print("Postorder:", bst.postorder())
        elif choice == '5':
            print("Depth of Tree:", bst.depth())
        elif choice == '6':
            bst.mirror()
            print("Tree mirrored.")
        elif choice == '7':
            copied_bst = bst.copy()
            print("Tree copied successfully.")
            if copied_bst:
                print("Copied Tree (Inorder):", copied_bst.inorder())
        elif choice == '8':
            pairs = bst.display_parents()
            if not pairs:
                print("No parent-child pairs (tree may be empty or single node).")
            else:
                print("Parent -> Children")
                for parent, children in pairs:
                    print(f"{parent} -> {children}")
        elif choice == '9':
            leaves = bst.display_leaves()
            print("Leaf Nodes:", leaves)
        elif choice == '10':
            levels = bst.level_order()
            for i, level in enumerate(levels):
                print(f"Level {i}: {level}")
        elif choice == '11':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
