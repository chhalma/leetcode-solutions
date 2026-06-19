from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Exercise 1 — LeetCode #104 Maximum Depth of Binary Tree

Return the maximum depth (number of nodes along the longest path from root to leaf).

    3
   / \
  9  20
    /  \
   15   7

→ 3

time: O(n)  space: O(h)
"""
def max_depth(root: TreeNode) -> int:
    if root is None:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1


"""
Exercise 2 — LeetCode #94 Binary Tree Inorder Traversal

Return the inorder traversal of a binary tree (left → root → right).

    1
     \
      2
     /
    3

→ [1,3,2]

time: O(n)  space: O(n)
"""
def inorder_traversal(root: TreeNode) -> list[int]:
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


"""
Exercise 3 — LeetCode #100 Same Tree

Given two binary trees, return true if they are structurally identical
with the same node values.

p=[1,2,3], q=[1,2,3] → True
p=[1,2],   q=[1,2,3] → False

time: O(n)  space: O(h)
"""
def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


"""
Exercise 4 — LeetCode #102 Binary Tree Level Order Traversal

Return the level order traversal as a list of lists.

    3
   / \
  9  20
    /  \
   15   7

→ [[3],[9,20],[15,7]]

time: O(n)  space: O(n)
"""
def level_order(root: TreeNode) -> list[list[int]]:
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
