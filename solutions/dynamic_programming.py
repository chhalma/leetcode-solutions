"""
Exercise 1 — LeetCode #70 Climbing Stairs


You can climb 1 or 2 steps at a time.
How many ways to reach step n?

n=2 → 2  (1+1, 2)
n=3 → 3  (1+1+1, 1+2, 2+1)
n=5 → 8

time: O(n) space: (n)
"""

def climbing_steps(n:int)->int:

     if n <= 2:
          return n
     dp = [0]*(n+1)
     dp[1] = 1
     dp[2] = 2
     for i in range(3,n+1,1):
          dp[i] = dp[i-1] + dp[i-2]
     return dp[n]
#O(n) space(1)
def climbing_optimized(n:int)->int:
     if n <= 2:
          return n
     prev2 = 1
     prev1 = 2

     for i in range(3,n+1):
          curr = prev1 +prev2
          prev2 = prev1
          prev1 = curr
     return prev1

"""
Exercise 2 — LeetCode #198 House Robber


Rob houses in a row — can't rob two adjacent houses.
Return max amount you can rob.

nums=[1,2,3,1]  → 4  (rob house 0 and 2)
nums=[2,7,9,3,1] → 12 (rob house 0, 2, 4)

O(n)  space O(1)
"""
def max_rob(nums:list[int])->int:
     if len(nums) == 1:
          return nums[0]
     dp = [0] * len(nums)
     dp[0] = nums[0]
     dp[1] = max(nums[0], nums[1])

     for i in range(2, len(nums)):
          dp[i] = max(dp[i-1] ,  dp[i-2]+nums[i])

     return dp[-1]

def max_rob_opt(nums:list[int])->int:
     prev1 = 0
     prev2 = 0
     for n in nums:
          curr = max(prev1, prev2+n)
          prev2 = prev1
          prev1 = curr
          
     return prev1

"""
Exercise 3 — LeetCode #1143 Longest Common Subsequence


Given two strings, return length of their 
longest common subsequence.

s1="abcde", s2="ace"  → 3  ("ace")
s1="abc",   s2="abc"  → 3
s1="abc",   s2="def"  → 0

time: O(mn) space : O(mn)
"""
def common_sub(s1:str, s2:str)->int:
     m,n = len(s1),len(s2)
     dp = [[0]*(n+1) for _ in range(m+1)]

     for i in range(1, m+1):
          for j in range(1, n+1):
               if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
               else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
     return dp[m][n]
"""
Exercise 4 — LeetCode #322 Coin Change


Given coins and a target amount, return the 
minimum number of coins to make the amount.
Return -1 if impossible.

coins=[1,5,10], amount=11  → 2  (10+1)
coins=[2],      amount=3   → -1

time: O(n x m) and space:O(m)

"""

def coin_change(coins:list[int],amount:int)->int:
     
     dp = [0]+[float('inf')]*amount

     for i in range(1, amount+1):
          for coin in coins:
               if coin <= i:
                    dp[i] = min(dp[i],dp[i-coin]+1)
     
     return dp[amount] if dp[amount] != float('inf') else -1