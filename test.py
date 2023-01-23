class Solution(object):
    def __init__(self):
        self.count1=0
        self.count2=0
    
    def countUnivalSubtrees(self, root):
        if not root:
            return 0
        if not root.left and not root.right: 
            self.count1 += 1
            return 1
        
        return self.countUnivalSubtrees(root.left) + self.countUnivalSubtrees(root.right) + (1 if self.same(root, root.val) else 0)

    def same(self, root, val):
        if not root: return True
        if root.val != val: return False
        return self.same(root.left, val) and self.same(root.right, val)
