'''
Balanced BST:
AVL
Insert, delete, min, max O(h) -> height of tree 
h = O(logn) | worst O(2logn)
For every node, require heights of left and right child to defer by +-1
echo node stores the height
'''
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Height of node (leaf = 1)

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node == None:
            return AVLNode(key)
        
        # left child
        if node.key > key:
            node.left = self._insert(node.left, key)

        # right child
        if node.key <= key:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        
        return self._balance(node)

    def _get_height(self, node):
        return node.height if node else 0

    '''
        0 -> balanced
        > 1 and -> left is bigger | right rotate
        < 0 and -> right is bigger | left rotate
    '''
    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _balance(self, node):
        balance = self._get_balance(node)
        if not balance:
            return node
        
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        
        if balance < 1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        # update the heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _right_rotate(self, z):
        y = z.left
        T2 = y.right

        y.right = z
        z.left = T2

        # update the heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)

# Example Usage
avl = AVLTree()
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    avl.insert(key)

avl.inorder_traversal(avl.root)  # Output: 10 20 25 30 40 50 (Balanced BST)
