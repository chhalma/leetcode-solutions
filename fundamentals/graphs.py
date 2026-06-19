from collections import deque


"""
Exercise 1 — LeetCode #200 Number of Islands

Given a 2D grid of '1's (land) and '0's (water), count the number of islands.

grid=[["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]] → 1

grid=[["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]] → 3

time: O(rows × cols)  space: O(rows × cols)
"""
def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    return count


"""
Exercise 2 — Graph DFS (adjacency list)

Given a graph and source node, return all reachable nodes via DFS.

graph={0:[1,2], 1:[3], 2:[3], 3:[]}
dfs(graph, 0) → [0,2,3,1] (order may vary)

time: O(V+E)  space: O(V)
"""
def dfs(graph: dict, src: int) -> list[int]:
    visited = set()
    stack = [src]
    result = []
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
    return result


"""
Exercise 3 — Graph BFS (adjacency list)

Given a graph and source node, return all reachable nodes via BFS.
BFS finds shortest path; DFS does not.

graph={0:[1,2], 1:[3], 2:[3], 3:[]}
bfs(graph, 0) → [0,1,2,3]

time: O(V+E)  space: O(V)
"""
def bfs(graph: dict, src: int) -> list[int]:
    visited = set([src])
    queue = deque([src])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result


"""
Exercise 4 — Has Path (BFS)

Given a directed graph, source, and destination, return true if a path exists.

graph={0:[1,2], 1:[3], 2:[3], 3:[]}
has_path(graph, 0, 3) → True
has_path(graph, 3, 0) → False

time: O(V+E)  space: O(V)
"""
def has_path(graph: dict, src: int, dest: int) -> bool:
    if src == dest:
        return True
    visited = set()
    queue = deque([src])
    while queue:
        node = queue.popleft()
        if node == dest:
            return True
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            queue.append(neighbor)
    return False
