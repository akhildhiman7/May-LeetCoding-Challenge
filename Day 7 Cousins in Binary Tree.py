'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.



Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false


Constraints:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        q = [root, None]
        temp = []
        while len(q) > 1:
            a = q[0]
            del q[0]
            if a == None:
                x_val, y_val = False, False
                for xxx in temp:
                    if xxx == x:
                        x_val = True
                    if xxx == y:
                        y_val = True
                if x_val | y_val:
                    print("UPPR NICHE")
                    return x_val & y_val
                if q[0] == None:
                    break
                temp.clear()
                q.append(None)
                continue
            flg = True
            if a.left:
                if a.left.val == x or a.left.val == y:
                    flg = False
                temp.append(a.left.val)
                q.append(a.left)
            if a.right:
                if a.right.val == x or a.right.val == y:
                    if not flg:
                        print("BHAI BHAI")
                        return False
                temp.append(a.right.val)
                q.append(a.right)
        print("LAST M SE")
        return False
