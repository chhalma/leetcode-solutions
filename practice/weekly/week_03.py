"""Week 3 — Revision (Week 1 + Week 2, no hints, no solutions)"""

"""
Day 1
"""

"""
#1 Two Sum  [Easy]

Given an array and target, return indices of two numbers that add to target.

nums=[2,7,11,15], target=9 → [0,1]
nums=[3,2,4],     target=6 → [1,2]
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for i,n in enumerate(nums):
        inv = target - n
        if inv in seen:
            index =  seen.get(inv)
            return [i, index]
        else:
            seen[n] = i
    return None


"""
#322 Coin Change  [Medium]

Given coins and an amount, return fewest coins to make up amount.
Return -1 if not possible.

coins=[1,2,5], amount=11 → 3  (5+5+1)
coins=[2],     amount=3  → -1
"""
def coin_change(coins: list[int], amount: int) -> int:
    dp = [float('inf')]*(amount+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2,amount+1):
        for c in coins:
            if c<=i:
                dp[i] = min(dp[i],dp[i-c]+1)
                
    return dp[amount] if dp[amount] != float('inf') else -1


"""
#200 Number of Islands  [Medium]

Given a 2D grid of '1's (land) and '0's (water), count the islands.

grid=[["1","1","0"],
      ["0","0","1"],
      ["0","0","1"]] → 2
"""
def num_islands(grid: list[list[str]]) -> int:
    rows =  len(grid)
    cols = len(grid[0])
    sum = 0
    def dfs(r,c):
        if r <0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        
        grid[r][c] = '0'
        dfs(r,c+1)
        dfs(r,c-1)
        dfs(r+1,c)
        dfs(r-1,c)
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                sum += 1
                dfs(i,j)
    return sum
           

"""
Day 2
"""

"""
#20 Valid Parentheses  [Easy]

Given a string of brackets, return true if it is valid.

s="()"     → True
s="()[]{}" → True
s="(]"     → False
"""
def is_valid(s: str) -> bool:
    pair = {'(':')', '{':'}','[':']'}
    stack = []
    closing = [')','}',']']
    for b in s:
        if b in pair:
            stack.append(b)
        elif b in closing:
            if not stack:
                return False
            opening = stack.pop()
            cl_br = pair[opening]
            if b != cl_br:
                return False
    if len(stack) == 0:
        return True


"""
#153 Find Minimum in Rotated Sorted Array  [Medium]

A sorted array was rotated at some pivot. Find the minimum element.

nums=[3,4,5,1,2]     → 1
nums=[4,5,6,7,0,1,2] → 0
"""
def find_min(nums: list[int]) -> int:
    left = 0
    right = len(nums)-1
    
    while left<right:
        mid = (left+right)//2
        lv = nums[left]
        rv = nums[right]
        mv = nums[mid]

        if mv > rv:
            left = mid+1
        else:
            right = mid 
    return nums[left]


"""
Day 3
"""

"""
#70 Climbing Stairs  [Easy]

You can climb 1 or 2 steps at a time. How many ways to reach step n?

n=2 → 2
n=3 → 3
n=5 → 8
"""
def climb_stairs(n: int) -> int:
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    if n < 2:
        return n
    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]


"""
#543 Diameter of Binary Tree  [Medium]

Return the length of the longest path between any two nodes.

    1
   / \
  2   3
 / \
4   5
→ 3
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter_of_binary_tree(root: TreeNode) -> int:
     
    dia =  0

    def depth(node):
        nonlocal dia
        if not node:
            return 0
        left = depth(node.left)        
        right = depth(node.right)
        dia = max(dia, left+right)

        return 1 + max(left, right)
    
    depth(root)
    return dia
"""
Day 4
"""

"""
#121 Best Time to Buy and Sell Stock  [Easy]

Find the maximum profit from buying and selling once.
Must buy before you sell.

prices=[7,1,5,3,6,4] → 5
prices=[7,6,4,3,1]   → 0
"""

def max_profit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(price,min_price)
        profit =  price-min_price
        max_profit = max(max_profit,profit)
    return max_profit

def max_profit(prices:list[int]) ->int:
    left = 0
    max_profit= 0
    for right in range(1, len(prices)):
        if prices[right] > prices[left]:
            profit =  prices[right] - prices[left]
            max_profit = max(profit, max_profit)     
        else:
            left = right
    return max_profit       

"""
#226 Invert Binary Tree  [Medium]

Invert a binary tree (mirror it).

    4              4
   / \            / \
  2   7    →     7   2
"""
def invert_tree(root: TreeNode) -> TreeNode:
    
   if not root:
       return None
   
   root.left, root.right = root.right, root.left
   invert_tree(root.left)
   invert_tree(root.right)
   return root


"""
Day 5
"""

"""
#104 Maximum Depth of Binary Tree  [Easy]

Return the maximum depth of a binary tree.

    3
   / \
  9  20
    /  \
   15   7
→ 3
"""
def max_depth(root: TreeNode) -> int:
    if not root:
        return 0
        
    return 1+ max(max_depth(root.left),max_depth(root.right))    
    



"""
#21 Merge Two Sorted Lists  [Medium]

Merge two sorted linked lists and return the sorted result.

l1=1→2→4, l2=1→3→4 → 1→1→2→3→4→4
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    curr =  dummy

    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr =  curr.next
    
    curr.next = l1 or l2
    return dummy.next



"""
#3 Longest Substring Without Repeating Characters  [Medium]

Find the length of the longest substring without repeating characters.

s="abcabcbb" → 3
s="bbbbb"    → 1
s="pwwkew"   → 3
"""
def length_of_longest_substring(s: str) -> int:
    pass
