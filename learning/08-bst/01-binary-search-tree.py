'''
BST:
O(logn)
but as if the BST is not balanced then searching or insertion will be O(n)
'''
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BST:
    def bst_insert(self, val, r) :
        if r == None:
            return Node(val)
        
        if r.val > val:
            r.left = self.bst_insert(val, r.left)
        else :
            r.right = self.bst_insert(val, r.right)

        return r
        
    def bst(self, ll) :
        lenOfll = len(ll)
        r = None
        for i in range(lenOfll):
            r = self.bst_insert(ll[i], r)

        return r

    def bst_find(self, r, val) :
        if r == None or r.val == None:
            return False
        key = None
        while key == None:
            if r.val == val:
                key = r.val
            
            if val > r.val:
                key = self.bst_find(r.right, val)

            if val < r.val:
                key = self.bst_find(r.left, val)

        return key

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)

if __name__ == "__main__":
    bst = BST()
    bst.inorder(bst.bst([2, 6, 1, 7, 9, 9, 4]))
    print('')
    bst.inorder(bst.bst([2, 6, 1, 7, 9, 9, 4, 99, 3, 1, 3, 98, 745, 7]))
    print('')
    print(bst.bst_find(bst.bst([2, 6, 1, 7, 9, 9, 4]), 22))
