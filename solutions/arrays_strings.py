"""
Exercise 1 — LeetCode #217 Contains Duplicate

Given an integer array, return true if any value appears at least twice.

nums=[1,2,3,1] → True
nums=[1,2,3,4] → False

time: O(n)  space: O(n)
"""
def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


"""
Exercise 2 — LeetCode #1 Two Sum

Given an array and target, return indices of two numbers that add to target.

nums=[2,7,11,15], target=9 → [0,1]
nums=[3,2,4],     target=6 → [1,2]

time: O(n)  space: O(n)
"""
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []


"""
Exercise 3 — LeetCode #242 Valid Anagram

Given two strings, return true if one is an anagram of the other.

s="anagram", t="nagaram" → True
s="rat",     t="car"     → False

time: O(n)  space: O(n)
"""
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    for c in t:
        if c not in freq:
            return False
        freq[c] -= 1
        if freq[c] < 0:
            return False
    return True


"""
Exercise 4 — LeetCode #49 Group Anagrams

Given a list of strings, group the anagrams together.

words=["eat","tea","tan","ate","nat","bat"] → [["eat","tea","ate"],["tan","nat"],["bat"]]

time: O(n * k log k)  space: O(n)
"""
from collections import defaultdict

def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())


"""
Exercise 5 — LeetCode #347 Top K Frequent Elements

Return the k most frequent elements.

nums=[1,1,1,2,2,3], k=2 → [1,2]

time: O(n log k)  space: O(n)
"""
# Solution 1
# Time O(nlogn) space(n)
from collections import Counter

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    return [num for num, _ in Counter(nums).most_common(k)]

# Solution 2
# Time O(nlogn) space(n)
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    freq = defaultdict(int)

    for n in nums:
        freq[n] += 1
    sorted_freq = sorted(freq, key=lambda x: freq[x], reverse=True)
    return sorted_freq[:k]

# Solution 3
# Time O(nlogk) space(n)
import heapq   
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    freq = Counter(nums)
    heap = []

    for  n, c in freq.items():
        heapq.heappush(heap,(c,n))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for count,num in heap ]

"""
Exercise 6 — LeetCode #560 Subarray Sum Equals K

Return the number of subarrays that sum to k.

nums=[1,1,1], k=2 → 2
nums=[1,2,3], k=3 → 2

time: O(n)  space: O(n)
"""
def subarray_sum(nums: list[int], k: int) -> int:
    seen = {0: 1}
    prefix = 0
    count = 0
    for n in nums:
        prefix += n
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count



"""
Exercise 7 — LeetCode #125 Valid Palindrome

A phrase is a palindrome if it reads the same forwards and backwards
(ignoring non-alphanumeric characters and case).

s="A man, a plan, a canal: Panama" → True
s="race a car"                     → False

time: O(n)  space: O(1)
"""
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


"""
Exercise 8 — LeetCode #3 Longest Substring Without Repeating Characters

Return the length of the longest substring without repeating characters.

s="abcabcbb" → 3  ("abc")
s="bbbbb"    → 1  ("b")

time: O(n)  space: O(n)
"""
def length_of_longest_substring(s: str) -> int:
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len


"""
Exercise 9 — LeetCode #643 Maximum Average Subarray I

Find the contiguous subarray of length k with the maximum average.

nums=[1,12,-5,-6,50,3], k=4 → 12.75

time: O(n)  space: O(1)
"""
def find_max_average(nums: list[int], k: int) -> float:
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum / k


def find_max_average(nums: list[int], k: int) -> float:
    max_avg = 0.0
    
    for i in range(len(nums)):
        j = i
        sum = 0.0
        windpw_size = k
        while windpw_size > 0:
            sum +=nums[j]
            windpw_size -= 1
            j +=1
        max_avg = max(max_avg, sum/k)
    return max_avg
