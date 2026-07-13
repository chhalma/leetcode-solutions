"""Week 4 — Daily Practice"""

"""
Day 1 — LeetCode #572 Subtree of Another Tree

Given roots of two binary trees root and subRoot, return true if
there is a subtree of root with the same structure and node values as subRoot.

root=    [3,4,5,1,2]     subRoot=[4,1,2]  → True
root=    [3,4,5,1,2,null,null,null,null,0]  subRoot=[4,1,2]  → False

3 versions to solve:
  v1. DFS + same tree check  — O(m×n) time  O(h) space  [check every node]
  v2. Serialize + string match — O(m+n) time  O(m+n) space  [convert to string]
  v3. Recursive helper        — O(m×n) time  O(h) space  [cleaner split of concerns]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_subtree_v1(root: TreeNode, subRoot: TreeNode) -> bool:
    def sameTree(r,s)-> bool:
        if not r and not s:
            return True
        if not r or not s:
            return False
        return r.val == s.val and sameTree(r.left,s.left) and sameTree(r.right,s.right)

    if not root:
        return False
    if sameTree(root, subRoot):
        return True
    return is_subtree_v1(root.left, subRoot) or is_subtree_v1(root.right, subRoot)    

def is_subtree_v2(root: TreeNode, subRoot: TreeNode) -> bool:
    def ser(n)->str:
        if not n:
            return "#N"
        return "#" + str(n.val) +ser(n.left) +ser(n.right)
    
    return ser(subRoot) in ser(root)

def same_tree(s, t):
    if not s and not t: return True
    if not s or not t: return False
    return s.val == t.val and same_tree(s.left, t.left) and same_tree(s.right, t.right)

def is_subtree_v3(root, subRoot):
    if not root: return False
    if same_tree(root, subRoot): return True
    return is_subtree_v3(root.left, subRoot) or is_subtree_v3(root.right, subRoot)

"""
Day 2 — LeetCode #235 Lowest Common Ancestor of a BST

Given a BST and two nodes p and q, find their lowest common ancestor.
LCA is the lowest node that has both p and q as descendants.

BST:        6
           / \
          2   8
         / \ / \
        0  4 7  9
          / \
         3   5

p=2, q=8 → 6
p=2, q=4 → 2

2 versions to solve:
  v1. Recursive  — O(h) time  O(h) space  [compare values with root]
  v2. Iterative  — O(h) time  O(1) space  [walk down the tree]
"""
def lca_bst_v1(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    pass

def lca_bst_v2(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    pass


"""
Day 3 — LeetCode #102 Binary Tree Level Order Traversal

Return the level-order traversal of a binary tree's values
(i.e., from left to right, level by level).

    3
   / \
  9  20
    /  \
   15   7

→ [[3],[9,20],[15,7]]

2 versions to solve:
  v1. BFS with queue   — O(n) time  O(n) space  [deque, process level by level]
  v2. DFS recursive    — O(n) time  O(n) space  [pass level index, build result]
"""
def level_order_v1(root: TreeNode) -> list[list[int]]:
    pass

def level_order_v2(root: TreeNode) -> list[list[int]]:
    pass


"""
Day 4 — LeetCode #207 Course Schedule

There are n courses. prerequisites[i]=[a,b] means to take a you must take b first.
Return true if you can finish all courses (no cycle).

n=2, prerequisites=[[1,0]]        → True
n=2, prerequisites=[[1,0],[0,1]]  → False (cycle)

2 versions to solve:
  v1. DFS cycle detection  — O(V+E) time  O(V+E) space  [visited states: 0=unvisited, 1=visiting, 2=done]
  v2. BFS topological sort — O(V+E) time  O(V+E) space  [Kahn's algorithm, in-degree]
"""
def can_finish_v1(numCourses: int, prerequisites: list[list[int]]) -> bool:
    pass

def can_finish_v2(numCourses: int, prerequisites: list[list[int]]) -> bool:
    pass


"""
Day 5 — LeetCode #46 Permutations

Given an array of distinct integers, return all possible permutations.

nums=[1,2,3] → [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
nums=[0,1]   → [[0,1],[1,0]]

2 versions to solve:
  v1. Backtracking        — O(n×n!) time  O(n) space   [classic backtrack, swap]
  v2. Built-in itertools  — O(n×n!) time  O(n×n!) space [know it exists, explain tradeoffs]
"""
def permute_v1(nums: list[int]) -> list[list[int]]:
    pass

def permute_v2(nums: list[int]) -> list[list[int]]:
    pass
