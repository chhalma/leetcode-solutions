# LeetCode Solutions

Python solutions for common algorithm and data structure problems, organised by topic.

## Topics Covered

| Topic | Problems |
|-------|----------|
| Sets & Hashmaps | Two Sum, Top K Frequent, Subarray Sum |
| Two Pointers | Palindrome, Reverse, Pair Finding |
| Sliding Window | Max Subarray (fixed), Longest Substring (dynamic) |
| Binary Search | Classic, Insert Position, Rotated Array, Merge Intervals |
| Trees | Max Depth, Inorder Traversal, Same Tree, Level Order BFS |
| Graphs | BFS, DFS, Number of Islands |
| Stacks & Heaps | Valid Parentheses, Min Stack, Kth Largest, Top K Frequent |
| Dynamic Programming | Climbing Stairs, House Robber, LCS, Coin Change |

## Files

- [dynamic_programming.py](dynamic_programming.py) — DP patterns with space-optimised variants

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
