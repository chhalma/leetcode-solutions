"""
Exercise 1 — LeetCode #238 Product of Array Except Self

Return array where output[i] = product of all elements except nums[i].
Do not use division.

nums=[1,2,3,4] → [24,12,8,6]
nums=[-1,1,0,-3,3] → [0,0,9,0,0]

time: O(n)  space: O(1)
"""
def product_except_self(nums: list[int]) -> list[int]:
    prod_left = []
    prod_right = []
    p_l = 1
    p_r = 1

    for i in range(len(nums)):
        prod_left.append(p_l)
        p_l *= nums[i]

    for i in range(len(nums) - 1, -1, -1):
        prod_right.append(p_r)
        p_r *= nums[i]

    prod_right.reverse()
    return [prod_left[i] * prod_right[i] for i in range(len(nums))]
   
"""
Exercise 2 — LeetCode #11 Container With Most Water

Array of heights. Find two lines that together with x-axis
forms a container holding the most water.

height=[1,8,6,2,5,4,8,3,7] → 49
height=[1,1] → 1

time: O(n)  space: O(1)
"""
def max_area(height: list[int]) -> int:
    left, right = 0, len(height)-1
    max_area = 0

    while left<right:
        area = min(height[left],height[right]) * (right-left)
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1 



"""
Exercise 3 — LeetCode #42 Trapping Rain Water

Given heights, compute how much water can be trapped.

height=[0,1,0,2,1,0,1,3,2,1,2,1] → 6
height=[4,2,0,3,2,5]              → 9

time: O(n)  space: O(1)
"""
def trap(height: list[int]) -> int:
    total_rain = 0
    
    while height[left] == 0:
        left += 1
        right +=1
        while height[right] == 0:
            right += 1

        rain_drop = min(height[left],height[right])*(right-left)
        total_rain += rain_drop
        left = right
        right +=1
    return total_rain



"""
Exercise 4 — LeetCode #76 Minimum Window Substring

Find the minimum window in s that contains all characters of t.

s="ADOBECODEBANC", t="ABC" → "BANC"
s="a", t="a"               → "a"
s="a", t="aa"              → ""

time: O(n)  space: O(n)
"""
def min_window(s: str, t: str) -> str:
    pass
