"""
1. LeetCode #743 Network Delay Time

n=4 nodes, times=[[2,1,1],[2,3,1],[3,4,1]], src=2
→ 2  (time for signal to reach all nodes from node 2)

times=[[1,2,1],[2,3,2]], src=1
→ 3
time: O((V+E)logV) space:O(V+E)
"""
import heapq
from collections import defaultdict
def network_delay(times:list[list[int]], n:int, src: int) ->int:
    graph =  defaultdict(list)

    for u,v,t in times:
        graph[u].append((v,t))

    heap = [(0,src)]
    visited = set()
    dist = {}

    while heap:
        cost, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        dist[node] = cost

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(heap,(cost+weight,neighbor))
    return max(dist.values()) if len(dist) == n else -1


"""
2. LeetCode #787 Cheapest Flights Within K Stops

n=4, flights=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src=0, dst=3, k=1
→ 700  (0→1→3, 1 stop)

src=0, dst=3, k=0
→ -1  (no direct flight)
time: O((V+E)logV) space: O(V+E)
"""

def cheapest_flights(n:int, flights:list[list[int]], src, dst , k:int)->int:
    graph = defaultdict(list)
    for u,v,w in flights:
        graph[u].append((v,w))

    heap = heapq[(0,0,src)]
    
    while heap:
        for cost, stops, node in heapq.heappop(heap):
            if node == dst:
                return cost
            if stops >k:
                continue
            
            for neigbor, weight in graph[node]:
                heapq.heappush(heap,(cost+weight,stops+1,neigbor))

    return -1


"""
3. LeetCode #1631 Path With Minimum Effort

heights=[[1,2,2],[3,8,2],[5,3,5]]
→ 2  (path 1→3→5→3→5, max effort=2)

heights=[[1,2,3],[3,8,4],[5,3,5]]
→ 1
time: O(r x c x log(r x c)) space: O(r x c)
"""

def path_minium_effort(heights:list[list[int]])->int:
    rows = len(heights)
    cols = len(heights[0])

    heap = [(0,0,0)]
    visited = set()
    directions = [(0,1),(0,-1),(1,0),(-1,0)]

    while heap:
        effort, r, c = heapq.heappop(heap)
        if (r,c) in visited:
            continue
        visited.add(r,c)
        
        if r == rows-1 and c == cols:
            return effort
        
        for dr, dc in directions:
            nr,nc = r+dr, c+dc
            if 0 <=nr<rows and c<= nc <cols and (nr,nc) not in visited:
                new_efort = max(effort, abs(heights[r][c]-heights([nr][nc])))
                heapq.heappush(new_efort,nr,nc)
    return -1
    
