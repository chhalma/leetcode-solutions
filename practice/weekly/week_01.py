"""Week 1 — Daily Practice"""

"""
Day 1 — LeetCode #1 Two Sum

Given an array and target, return indices of two numbers that add to target.

nums=[2,7,11,15], target=9 → [0,1]
nums=[3,2,4],     target=6 → [1,2]

Time: O(n) Space:O(n)
"""
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for i, n in enumerate(nums):
        inverse = target - n
        if inverse in seen:
            return [i, seen[inverse] ]
    
        seen[n] = i

    return None

# all possible unique way
#nums=[2,4,5,7,15], target=9 → [[0,3],[1,2]]

def two_sum_unique(nums: list[int], target: int):
    seen = {}
    results = []

    for i, n in enumerate(nums):
        complement = target - n

        if complement in seen:
            results.append([seen[complement], i])

        seen[n] = i

    return results

# all possible way
# nums=[3,3,3], target=6 → [[0,1],[0,2],[1,2]]

from collections import defaultdict

def two_sum_all(nums: list[int], target: int):
    seen = defaultdict(list)
    results = []

    for i, n in enumerate(nums):
        complement = target - n

        for j in seen[complement]:
            results.append([j, i])

        seen[n].append(i)

    return results
"""
Day 2 — LeetCode #20 Valid Parentheses

Given a string of brackets, return true if it is valid.

s="()"     → True
s="()[]{}" → True
s="(]"     → False
s="([)]"   → False

Time: O(n) Space: O(n)
"""
def is_valid(s: str) -> bool:
    pairs = {'(':')', '{':'}', '[':']'}
    valid_char = ['(',')','{','}','[',']']
    stack = []
    for b in s:
        if b not in valid_char:
            continue
        if b in pairs:
            stack.append(b)
        
        else:
            if not stack:
                return False
            
            c = stack.pop()
            if pairs[c] != b:
                return False

    return len(stack) == 0   


"""
Day 3 — LeetCode #104 Maximum Depth of Binary Tree

Return the maximum depth of a binary tree.

    3
   / \
  9  20
    /  \
   15   7

→ 3

3 versions to solve:
  v1. Recursive DFS     — O(n) time  O(h) space  [h=height, best case O(log n)]
  v2. Iterative DFS     — O(n) time  O(h) space  [explicit stack, no call stack]
  v3. BFS level order   — O(n) time  O(n) space  [count levels with a queue]
"""
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right =  right

def max_depth_v1(root: TreeNode) -> int:
    if not root:
        return 0
    
    return 1 + max(max_depth_v1(root.left), max_depth_v1(root.right))

def max_depth_v2(root: TreeNode) -> int:
    if not root:
        return 0
    
    stack = [(root, 1)]
    max_depth = 0

    while stack:
        node,depth = stack.pop()
        max_depth = max(max_depth, depth)

        if node.left :
            stack.append(node.left, depth+1)
        if node.right :
            stack.append(node.right, depth+1)

    return max_depth

from collections import deque
def max_depth_v3(root: TreeNode) -> int:
    if not root:
        return 0
    queue = deque([(root,1)])
    max_depth = 0

    while queue:
        node, depth = queue.popleft()

        max_depth = max(max_depth,depth)

        if node.left:
            queue.append((node.left,depth+1))
        if node.right:
            queue.append((node.right,depth+1))

    return max_depth
"""
Day 4 — LeetCode #200 Number of Islands

Given a 2D grid of '1's (land) and '0's (water), count the islands.

grid=[["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]] → 3

3 versions to solve:
  v1. DFS recursive     — O(m×n) time  O(m×n) space  [mark visited by mutating grid]
  v2. DFS iterative     — O(m×n) time  O(m×n) space  [explicit stack]
  v3. BFS               — O(m×n) time  O(m×n) space  [queue, spreads level by level]
"""


def num_islands_v1(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    def dfs(r,c):
        if r < 0 or r >= rows or c<0 or c >= cols or grid[r][c] != '1':
            return 
        grid[r][c] = '0'
        dfs(r, c+1)
        dfs(r,c-1)
        dfs(r+1,c)
        dfs(r-1,c)


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r,c)
    return count
                

def num_islands_v2(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                stack = [(r,c)]
                while stack:
                    row,col =  stack.pop()
                    if row < 0 or row>= rows or col <0 or col>=cols or grid[row][col] !='1':
                        continue
                    grid[row][col] = '0'
                    stack.append((row,col+1))
                    stack.append((row,col-1))
                    stack.append((row+1,col))
                    stack.append((row-1,col))
    return count

def num_islands_v3(grid: list[list[str]]) -> int:
    if not grid :
        return 0
    
    rows = len(grid)
    cols = len(grid[0])

    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1

                queue = deque([(r,c)])
                while queue:
                    row, col =  queue.popleft()
                    if row < 0 or row>= rows or col <0 or col>=cols or grid[row][col] !='1':
                        continue
                    grid[row][col] = '0'
                    queue.append((row,col+1))
                    queue.append((row,col-1))
                    queue.append((row+1,col))
                    queue.append((row-1,col))
    return count


"""
Day 5 — LeetCode #70 Climbing Stairs

You can climb 1 or 2 steps at a time. How many ways to reach step n?

n=2 → 2
n=3 → 3
n=5 → 8

3 versions to solve:
  v1. DP array          — O(n) time  O(n) space   [dp[i] = dp[i-1] + dp[i-2]]
  v2. DP two variables  — O(n) time  O(1) space   [only keep last two values]
  v3. Recursion + memo  — O(n) time  O(n) space   [top-down with cache]
"""
def climb_stairs_v1(n: int) -> int:
    pass

def climb_stairs_v2(n: int) -> int:
    pass

def climb_stairs_v3(n: int) -> int:
    pass


"""
Day 6 — LeetCode #21 Merge Two Sorted Lists

Merge two sorted linked lists and return the sorted result.

l1=1→2→4, l2=1→3→4 → 1→1→2→3→4→4

3 versions to solve:
  v1. Iterative dummy   — O(n+m) time  O(1) space   [dummy head, walk both lists]
  v2. Recursive         — O(n+m) time  O(n+m) space [call stack grows with length]
  v3. In-place no dummy — O(n+m) time  O(1) space   [track head manually, no dummy]
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists_v1(l1: ListNode, l2: ListNode) -> ListNode:
    pass

def merge_two_lists_v2(l1: ListNode, l2: ListNode) -> ListNode:
    pass

def merge_two_lists_v3(l1: ListNode, l2: ListNode) -> ListNode:
    pass


"""
Day 7 — LeetCode #121 Best Time to Buy and Sell Stock

Find the maximum profit from buying and selling once.
Must buy before you sell.

prices=[7,1,5,3,6,4] → 5  (buy at 1, sell at 6)
prices=[7,6,4,3,1]   → 0  (no profit possible)

3 versions to solve:
  v1. Two pointers      — O(n) time  O(1) space   [min_price + max_profit tracking]
  v2. One pass min track— O(n) time  O(1) space   [same idea, written differently]
  v3. Brute force       — O(n²) time O(1) space   [every pair, know why it's slow]
"""
def max_profit_v1(prices: list[int]) -> int:
    pass

def max_profit_v2(prices: list[int]) -> int:
    pass

def max_profit_v3(prices: list[int]) -> int:
    pass
