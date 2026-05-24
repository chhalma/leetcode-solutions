class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Exercise 1 — LeetCode #543 Diameter of Binary Tree

Return the length of the longest path between any two nodes.
Path does not need to pass through root.

    1
   / \
  2   3
 / \
4   5

→ 3  (path 4→2→1→3 or 4→2→5, length = 3 edges)

time: O(n)  space: O(h)
"""
def diameter_of_binary_tree(root: TreeNode) -> int:
    pass


"""
Exercise 2 — LeetCode #572 Subtree of Another Tree

Given root and subRoot, return true if subRoot is a subtree of root.

root=        subRoot=
    3            4
   / \          / \
  4   5        1   2
 / \
1   2

→ True

time: O(n×m)  space: O(h)
"""
def is_subtree(root: TreeNode, subRoot: TreeNode) -> bool:
    pass


"""
Exercise 3 — LeetCode #235 Lowest Common Ancestor of BST

Given a BST and two nodes p and q, return their lowest common ancestor.
LCA = deepest node that has both p and q as descendants.

        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3   5

p=2, q=8 → 6
p=2, q=4 → 2

time: O(h)  space: O(1)
"""
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    pass


"""
Exercise 4 — LeetCode #105 Construct Binary Tree from Preorder and Inorder

Given preorder and inorder traversal arrays, construct the binary tree.

preorder=[3,9,20,15,7]
inorder= [9,3,15,20,7]

→     3
     / \
    9  20
      /  \
     15   7

time: O(n)  space: O(n)
"""
def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode:
    pass
