"""Week 2 — Daily Practice"""

"""
Day 1 — LeetCode #153 Find Minimum in Rotated Sorted Array

A sorted array was rotated at some pivot. Find the minimum element.

nums=[3,4,5,1,2]   → 1
nums=[4,5,6,7,0,1,2] → 0
nums=[11,13,15,17]  → 11

2 versions to solve:
  v1. Binary search     — O(log n) time  O(1) space  [compare mid with right]
  v2. Linear scan       — O(n) time      O(1) space  [brute force, know why it's slow]
"""
def find_min_v1(nums: list[int]) -> int:
    left = 0 
    right = len(nums)-1

    while left < right:
        mid = (left+right)//2
        val = nums[mid]
        if val > nums[right]:
            left = mid+1
        else:
            right = mid

    return nums[left]

def find_min_v2(nums: list[int]) -> int:
    
    for i in range(len(nums)-1):
       if nums[i+1] < nums[i]:
           return nums[i+1]
       else:
           return nums[i]
       

"""
Day 2 — LeetCode #226 Invert Binary Tree

Invert a binary tree (mirror it).

    4              4
   / \            / \
  2   7    →     7   2
 / \ / \        / \ / \
1  3 6  9      9  6 3  1

3 versions to solve:
  v1. Recursive         — O(n) time  O(h) space  [swap left/right, recurse]
  v2. Iterative BFS     — O(n) time  O(n) space  [queue, swap at each level]
  v3. Iterative DFS     — O(n) time  O(h) space  [stack, swap as you go]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree_v1(root: TreeNode) -> TreeNode:
    if not root:
        return
    root.left, root.right =  root.right, root.left
    invert_tree_v1(root.left)
    invert_tree_v1(root.right)
    return root

from collections import deque 
def invert_tree_v2(root: TreeNode) -> TreeNode:
     
     if not root:
         return None
     queue = deque([root])

     while queue:
         node =  queue.popleft()
             
         left = node.left
         node.left =  node.right
         node.right = left
         if node.left != None:
            queue.append(node.left)
         if node.right != None:
            queue.append(node.right)
     return root

    

def invert_tree_v3(root: TreeNode) -> TreeNode:
    if not root:
        return
    
    stack = [root]

    while stack:
        node = stack.pop()
        left = node.left
        node.left =  node.right
        node.right = left
        if node.left != None:
            stack.append(node.left)
        if node.right != None:
            stack.append(node.right)
    return root



"""
Day 3 — LeetCode #543 Diameter of Binary Tree

Return the length of the longest path between any two nodes.
The path may or may not pass through the root.

    1
   / \
  2   3     → 3  (path: 4→2→1→3 or 5→2→1→3)
 / \
4   5

2 versions to solve:
  v1. DFS with nonlocal  — O(n) time  O(h) space  [track max diameter as global]
  v2. DFS return tuple   — O(n) time  O(h) space  [return (depth, diameter) pair]
"""
def diameter_of_binary_tree_v1(root: TreeNode) -> int:
    diameter = 0

    def depth(node):
        nonlocal diameter
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)

        diameter = max(diameter, left+right)
        return 1+ max(left,right)

    depth(root)
    return diameter
    
def diameter_of_binary_tree_v2(root: TreeNode) -> int:
    def depth(node):
        if not node:
            return (0,0)
        left_dpth, left_dia =  depth(node.left)
        right_dpth, right_dia = depth(node.right)
        cur_dia = left_dpth+right_dpth
        max_dia = max(cur_dia, left_dia,right_dia)

        return (1+max(left_dpth,right_dpth), max_dia)
        
    return depth(root)[1]

"""
Day 4 — LeetCode #322 Coin Change

Given coins and an amount, return fewest coins to make up amount.
Return -1 if not possible.

coins=[1,5,11], amount=15 → 3  (5+5+5 or 1+3*... wait: 11+1+1+1+1=5? No. 5+5+5=3 ✓)
coins=[1,2,5],  amount=11 → 3  (5+5+1)
coins=[2],      amount=3  → -1

3 versions to solve:
  v1. Bottom-up DP      — O(amount × coins) time  O(amount) space
  v2. Top-down memo     — O(amount × coins) time  O(amount) space
  v3. BFS               — O(amount × coins) time  O(amount) space  [treat as shortest path]
"""
def coin_change_v1(coins: list[int], amount: int) -> int:
    
    dp = [float('inf')]*(amount+1)
    dp[0] = 0
    
    for i in range(1, amount+1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_v2(coins: list[int], amount: int) -> int:
    
    memo = {}
    def helper(remaining):
        if remaining == 0:
            return 0
        if remaining < 0 :
            return -1
        if remaining in memo:
            return memo[remaining]
        
        min_coin = float('inf')
        for coin in coins:
            result = helper(remaining-coin)
            if result != -1:
                min_coin = min(min_coin,result+1)

        memo[remaining] =  min_coin if min_coin != float('inf') else -1
        return memo[remaining]

    return helper(amount)


def coin_change_v3(coins: list[int], amount: int) -> int:
    pass


"""
Day 5 — LeetCode #3 Longest Substring Without Repeating Characters

Find the length of the longest substring without repeating characters.

s="abcabcbb" → 3  ("abc")
s="bbbbb"    → 1  ("b")
s="pwwkew"   → 3  ("wke")

2 versions to solve:
  v1. Sliding window + set   — O(n) time  O(n) space  [shrink window on duplicate]
  v2. Sliding window + dict  — O(n) time  O(n) space  [jump left pointer directly]
"""
def length_of_longest_substring_v1(s: str) -> int:
    pass

def length_of_longest_substring_v2(s: str) -> int:
    pass
