import heapq
from collections import Counter


"""
Exercise 1 — LeetCode #20 Valid Parentheses

Given a string of brackets, return true if it is valid.
Valid means every opening bracket has a matching closing bracket in order.

s="()"     → True
s="()[]{}" → True
s="(]"     → False

time: O(n)  space: O(n)
"""
def is_valid(s: str) -> bool:
    pairs = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for c in s:
        if c in pairs:
            stack.append(c)
        else:
            if not stack or pairs[stack[-1]] != c:
                return False
            stack.pop()
    return len(stack) == 0


"""
Exercise 2 — LeetCode #155 Min Stack

Stack that supports push, pop, top, and retrieving the minimum in O(1).

min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
min_stack.get_min() → -3
min_stack.pop()
min_stack.top()     → 0
min_stack.get_min() → -2

time: O(1) all ops  space: O(n)
"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]


"""
Exercise 3 — LeetCode #703 Kth Largest Element in a Stream

Find the kth largest element in a stream of numbers.

k=3, nums=[4,5,8,2]
add(3)  → 4
add(5)  → 5
add(10) → 8
add(9)  → 8
add(4)  → 8

time: O(n log k)  space: O(k)
"""
class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


"""
Exercise 4 — LeetCode #347 Top K Frequent Elements (heap approach)

Return the k most frequent elements using a min-heap.

nums=[1,1,1,2,2,3], k=2 → [1,2]

time: O(n log k)  space: O(n)
"""
from collections import Counter
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    freq = Counter(nums)
    heap = []
    for num, count in freq.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for count, num in heap]

