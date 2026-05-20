"""
Exercise 1 — LeetCode #704 Binary Search

Given a sorted array and target, return the index or -1 if not found.

nums=[-1,0,3,5,9,12], target=9 → 4
nums=[-1,0,3,5,9,12], target=2 → -1

time: O(log n)  space: O(1)
"""
def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


"""
Exercise 2 — LeetCode #35 Search Insert Position

Given a sorted array and target, return the index if found,
or where it would be inserted.

nums=[1,3,5,6], target=5 → 2
nums=[1,3,5,6], target=2 → 1
nums=[1,3,5,6], target=7 → 4

time: O(log n)  space: O(1)
"""
def search_insert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


"""
Exercise 3 — LeetCode #153 Find Minimum in Rotated Sorted Array

Find the minimum element in a rotated sorted array.

nums=[3,4,5,1,2] → 1
nums=[4,5,6,7,0,1,2] → 0

time: O(log n)  space: O(1)
"""
def find_min(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


"""
Exercise 4 — LeetCode #56 Merge Intervals

Given a list of intervals, merge all overlapping intervals.

intervals=[[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]
intervals=[[1,4],[4,5]]               → [[1,5]]

time: O(n log n)  space: O(n)
"""
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= res[-1][1]:
            res[-1][1] = max(res[-1][1], end)
        else:
            res.append([start, end])
    return res
