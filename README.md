# LeetCode Solutions

Python solutions for common algorithm and data structure problems, organised by topic.

## Files

| File | Problems |
|------|----------|
| [arrays_strings.py](solutions/arrays_strings.py) | #217 Contains Duplicate, #1 Two Sum, #242 Valid Anagram, #49 Group Anagrams, #347 Top K Frequent, #560 Subarray Sum, #125 Valid Palindrome, #3 Longest Substring, #643 Max Average Subarray |
| [binary_search.py](solutions/binary_search.py) | #704 Binary Search, #35 Search Insert Position, #153 Find Minimum Rotated Array, #56 Merge Intervals |
| [trees.py](solutions/trees.py) | #104 Max Depth, #94 Inorder Traversal, #100 Same Tree, #102 Level Order Traversal |
| [graphs.py](solutions/graphs.py) | #200 Number of Islands, Graph DFS, Graph BFS, Has Path |
| [stacks_heaps.py](solutions/stacks_heaps.py) | #20 Valid Parentheses, #155 Min Stack, #703 Kth Largest, #347 Top K Frequent (heap) |
| [dynamic_programming.py](solutions/dynamic_programming.py) | #70 Climbing Stairs, #198 House Robber, #1143 LCS, #322 Coin Change |
| [linked_lists.py](solutions/linked_lists.py) | #206 Reverse Linked List, #21 Merge Two Sorted Lists, #141 Linked List Cycle, #876 Middle of Linked List, #19 Remove Nth From End |
| [dijkstra_graph.py](solutions/dijkstra_graph.py) | #743 Network Delay Time, #787 Cheapest Flights Within K Stops, #1631 Path With Minimum Effort |

## Revision Notes

- [patterns_learned.md](patterns_learned.md) — all patterns, when to use what, Python cheatsheet

## Key Patterns

- **Two Pointers** — O(n) pair/palindrome problems on sorted arrays
- **Sliding Window** — fixed and dynamic size subarray/substring problems
- **Prefix Sum + Hashmap** — subarray sum problems in O(n)
- **Binary Search** — classic, insert position, rotated array
- **BFS/DFS** — trees (level order, traversal), graphs (adjacency list), grids (islands)
- **Heaps** — kth largest, top k frequent using `heapq` (min-heap)
- **Dynamic Programming** — 1D and 2D DP, space-optimised variants

## Complexity Quick Reference

| Pattern | Time | Space |
|---------|------|-------|
| Two Pointers | O(n) | O(1) |
| Sliding Window | O(n) | O(1) or O(n) |
| Binary Search | O(log n) | O(1) |
| BFS / DFS | O(V+E) | O(V) |
| 1D DP | O(n) | O(n) → O(1) optimised |
| 2D DP (LCS) | O(m×n) | O(m×n) |
| Coin Change DP | O(amount × coins) | O(amount) |

## Language

Python 3
