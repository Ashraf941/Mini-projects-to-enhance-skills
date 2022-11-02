from logging import exception


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        
        current = self.root
        while True:
            if new_val < current.value:
                if current.left == None:
                    current.left = Node(new_val)
                    return
                else:
                    current = current.left
            elif new_val > current.value:
                if current.right == None:
                    current.right = Node(new_val)
                    return
                else:
                    current = current.right
            else:
                print("BSTs don't allow duplicates")

    def search(self, find_val):
        
        current = self.root
        while current.right or current.left:
            if current.value == find_val:
                return True
            elif find_val < current.value:
                 current = current.left
            elif find_val > current.value:
                current = current.right
        
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))