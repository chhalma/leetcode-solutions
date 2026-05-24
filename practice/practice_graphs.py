from collections import deque


"""
Exercise 1 — LeetCode #207 Course Schedule

There are n courses. prerequisites[i]=[a,b] means to take a you must take b first.
Return true if you can finish all courses (no cycle).

n=2, prerequisites=[[1,0]]         → True
n=2, prerequisites=[[1,0],[0,1]]   → False (cycle)

time: O(V+E)  space: O(V+E)
"""
def can_finish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    pass


"""
Exercise 2 — LeetCode #417 Pacific Atlantic Water Flow

Grid of heights. Water flows to adjacent cells with equal or lower height.
Pacific ocean borders top and left. Atlantic borders bottom and right.
Return all cells where water can flow to BOTH oceans.

heights=[[1,2,2,3,5],
         [3,2,3,4,4],
         [2,4,5,3,1],
         [6,7,1,4,5],
         [5,1,1,2,4]]

→ [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

time: O(rows × cols)  space: O(rows × cols)
"""
def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    pass


"""
Exercise 3 — LeetCode #133 Clone Graph

Given a node in a connected undirected graph, return a deep copy.
Each node has a val and a list of neighbors.

1 -- 2
|    |
4 -- 3

→ deep copy of same structure

time: O(V+E)  space: O(V)
"""
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node: Node) -> Node:
    pass


"""
Exercise 4 — LeetCode #994 Rotting Oranges

Grid: 0=empty, 1=fresh, 2=rotten. Each minute rotten oranges
spread to adjacent fresh oranges. Return minutes until no fresh remain.
Return -1 if impossible.

[[2,1,1],
 [1,1,0],
 [0,1,1]] → 4

[[0,2]] → 0

time: O(rows × cols)  space: O(rows × cols)
"""
def oranges_rotting(grid: list[list[int]]) -> int:
    pass
