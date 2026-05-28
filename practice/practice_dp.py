"""
Exercise 1 — LeetCode #300 Longest Increasing Subsequence

Return the length of the longest strictly increasing subsequence.

nums=[10,9,2,5,3,7,101,18] → 4  ([2,3,7,101])
nums=[0,1,0,3,2,3]         → 4
nums=[7,7,7,7]              → 1

time: O(n²)  space: O(n)
"""
def length_of_lis(nums: list[int]) -> int:
    dp = [1] * len(nums)
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)



"""
Exercise 2 — LeetCode #139 Word Break

Given a string and a list of words, return true if the string
can be segmented into words from the list.

s="leetcode",  wordDict=["leet","code"]       → True
s="applepenapple", wordDict=["apple","pen"]   → True
s="catsandog", wordDict=["cats","dog","sand"] → False

time: O(n²)  space: O(n)
"""
def word_break(s: str, wordDict: list[str]) -> bool:
    pass


"""
Exercise 3 — LeetCode #416 Partition Equal Subset Sum

Given an array, return true if it can be partitioned into
two subsets with equal sum.

nums=[1,5,11,5] → True   ([1,5,5] and [11])
nums=[1,2,3,5]  → False

time: O(n × sum)  space: O(sum)
"""
def can_partition(nums: list[int]) -> bool:
    pass


"""
Exercise 4 — LeetCode #5 Longest Palindromic Substring

Return the longest palindromic substring.

s="babad" → "bab"  (or "aba")
s="cbbd"  → "bb"

time: O(n²)  space: O(1)
"""
def longest_palindrome(s: str) -> str:
    pass
