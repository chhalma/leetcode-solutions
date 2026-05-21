# Patterns Learned

## Day 1 — Foundations
**Set for O(1) lookup**
- Use a set when you need to check existence instantly
- `seen = set()` → `if x in seen` is O(1)

**Frequency map (dict)**
- Count occurrences: `freq[x] = freq.get(x, 0) + 1`
- Find max: `max(freq, key=freq.get)`
- Or track running max inline to avoid final scan

**Hashmap (dict) — store and look up complement**
- Two Sum pattern: store `{value: index}`, look up `target - n`
- Key insight: store what you've seen, look up what you need

## Day 2 — Arrays & Strings
**Two Pointers**
- Two indices moving inward from both ends
- Use for: palindrome, reverse in place, pair finding on sorted arrays
- Pattern: `left, right = 0, len(arr)-1` → `while left < right`
- Python swap: `a, b = b, a` (no temp variable needed)

**Sliding Window — Fixed size**
- Build first window once with `sum(nums[:k])`
- Slide: `window_sum += nums[i] - nums[i-k]`
- Use for: max/min sum of subarray of size k
- Time O(n), Space O(1)

**Sliding Window — Dynamic size**
- Two pointers: left and right
- Expand right, shrink left when window becomes invalid
- `seen.remove(s[left]); left += 1` to shrink
- Use for: longest substring without repeating characters
- Time O(n), Space O(n)

## Day 3 — Hashmaps Deeper
**Anagram checking**
- Two freq dicts and compare: `dict1 == dict2`
- Or: `Counter(s) == Counter(t)` (cleaner)
- Or: `sorted(s) == sorted(t)` (O(n log n), simpler)

**Grouping with dict**
- Use a signature as key, list of matches as value
- `defaultdict(list)` — auto-creates empty lists
- Anagram key: `"".join(sorted(word))` or character count tuple
- Character count key: `tuple([0]*26)` with `ord(c) - ord('a')`

**Top K Frequent**
- `Counter(nums).most_common(k)` — built-in, returns sorted by frequency
- One liner: `[num for num, _ in Counter(nums).most_common(k)]`

**Prefix Sum + Hashmap**
- Running total: `prefix += n`
- If `prefix - k` seen before → subarray summing to k exists
- Start with `seen = {0: 1}` (empty subarray)
- Count occurrences in seen: `count += seen[prefix - k]`
- Use for: number of subarrays summing to k
- Time O(n), Space O(n)

## Day 4 — Binary Search + Sorting

**Binary Search template**
- Always: `left, right = 0, len(nums)-1` → `while left <= right` → `mid = (left+right)//2`
- Found: `return mid`
- Too small: `left = mid + 1`
- Too big: `right = mid - 1`
- Not found: `return -1`
- Time O(log n), Space O(1)

**Binary Search — Insert Position**
- Same template but `return left` when loop ends
- `left` is always where the element would be inserted

**Binary Search — Rotated Sorted Array**
- Compare `nums[mid]` with `nums[right]` only
- `nums[mid] > nums[right]` → min is in right half → `left = mid + 1`
- else → min is in left half or is mid → `right = mid`
- Use `while left < right` (not <=), return `nums[left]`

**Merge Intervals**
- Sort by start: `intervals.sort(key=lambda x: x[0])`
- Start res with first interval: `res = [intervals[0]]`
- For each next interval: if `start <= res[-1][1]` → overlap → `res[-1][1] = max(res[-1][1], end)`
- Else: append new interval
- Time O(n log n), Space O(n)

## Day 5 — Trees: BFS & DFS

**DFS — Max Depth (recursion)**
- Base case: `if tree is None: return 0`
- `return max(max_depth(tree.left), max_depth(tree.right)) + 1`
- Time O(n), Space O(h) where h = height

**DFS — Inorder Traversal**
- `return inorder(tree.left) + [tree.val] + inorder(tree.right)`
- Left → root → right. Use for BST (gives sorted order)

**BFS — Level Order**
- Use `deque`, start with root in queue
- `for _ in range(len(queue))` processes exactly one level
- Append left/right children for next level
- Time O(n), Space O(n)

**DFS — Same Tree**
- Both None → True
- One None → False
- Values differ → False
- `return same_tree(left, left) and same_tree(right, right)`

**When to use what:**
- Level-by-level → BFS + deque
- BST sorted order → Inorder DFS
- Everything else → DFS (recursion)

## Day 6 — Graphs: BFS & DFS

**Graph DFS (adjacency list)**
- Use a stack + visited set
- `stack.pop()` → LIFO
- `if neighbor not in visited: stack.append(neighbor)`
- Time O(V+E), Space O(V)

**Graph BFS (adjacency list)**
- Use `deque` + visited set
- `queue.popleft()` → FIFO
- Same logic as DFS, different data structure
- Finds shortest path, DFS does not

**Grid DFS (2D matrix — islands pattern)**
- Nested `dfs(r, c)` function inside main function
- Boundary check: `r < 0 or r >= rows or c < 0 or c >= cols`
- Mark visited by sinking: `grid[r][c] = '0'`
- 4 recursive calls: `dfs(r+1,c), dfs(r-1,c), dfs(r,c+1), dfs(r,c-1)`
- Outer loop: find unvisited '1' → count += 1 → dfs to sink island
- Time O(rows×cols), Space O(rows×cols)

**Has Path (BFS)**
- Check `if node == dest: return True` first
- Then guard with visited before adding neighbors
- `return False` after loop

**Key difference — DFS types:**
- Graph DFS: neighbors from `graph[node]` dict
- Grid DFS: neighbors from coordinates ±1

## Day 7 — Stacks & Heaps

**Valid Parentheses (stack)**
- `pairs = {'(':')', '{':'}', '[':']'}`
- Push opening brackets, pop and check on closing
- If stack empty on closing → return False
- Return `len(stack) == 0` at end

**Min Stack**
- Two stacks: `stack` and `min_stack`
- On push: `min_stack.append(min(val, min_stack[-1]))`
- On pop: pop both stacks together
- `get_min()` → `min_stack[-1]` always O(1)

**Kth Largest (min-heap of size k)**
- Push every element, if `len(heap) > k` → pop minimum
- `heap[0]` at end = kth largest
- Time O(n log k), Space O(k)

**Top K Frequent (heap)**
- Count with `Counter(nums)`
- Push `(count, num)` tuples — heap sorts by count
- If `len(heap) > k` → pop (removes least frequent)
- Extract: `[num for count, num in heap]`
- Time O(n log k), Space O(k)

**heapq rules:**
- `heapq.heappush(heap, val)` — push
- `heapq.heappop(heap)` — pop minimum
- `heap[0]` — peek minimum (no pop)
- Default is min-heap — negate values for max-heap
- Always push tuples `(sort_key, value)` when sorting by something other than value

## Day 8 — Dynamic Programming

**1D DP — Climbing Stairs (#70)**
- `dp[i] = dp[i-1] + dp[i-2]`
- Optimised: two variables `prev1, prev2`

**1D DP — House Robber (#198)**
- `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`
- Optimised: two variables `prev1, prev2`

**2D DP — Longest Common Subsequence (#1143)**
- `dp[i][j] = dp[i-1][j-1]+1` if chars match
- `dp[i][j] = max(dp[i-1][j], dp[i][j-1])` if not
- Time O(m×n), Space O(m×n)

**Coin Change (#322)**
- `dp = [0] + [float('inf')] * amount`
- `dp[i] = min(dp[i], dp[i-coin]+1)` for each coin
- Return `dp[amount]` if not inf else `-1`
- Time O(amount × coins), Space O(amount)

## Day 9 — Linked Lists

**Reverse Linked List (#206)**
- `prev=None, curr=head` → save `next_node`, reverse pointer, advance both
- `while curr` not `while curr.next` — process every node including last
- Return `prev` (new head)

**Merge Two Sorted Lists (#21)**
- Dummy node + `curr` builder pointer
- `while l1 and l2` → attach smaller, advance that pointer, advance curr
- After loop: `curr.next = l1 or l2` to attach remainder
- Return `dummy.next`

**Linked List Cycle (#141) — fast/slow**
- `slow=head, fast=head`
- `while fast and fast.next` → slow moves 1, fast moves 2
- If `fast == slow` → cycle exists
- Return `False` after loop

**Middle of Linked List (#876) — fast/slow**
- Same as cycle but just return `slow` when loop ends
- Even length → naturally returns second middle

**Remove Nth From End (#19)**
- Dummy node + `slow=dummy, fast=dummy`
- Move fast n steps ahead FIRST (outside while loop)
- Then move both until `fast.next is None`
- `slow.next = slow.next.next` → skip the node
- Return `dummy.next` (not head — head may be deleted)

## Day 10 — Dijkstra

**Dijkstra pattern**
- `heap = [(0, src)]` → always `(cost, node)`
- `visited = set()` — skip already processed nodes
- `dist = {}` — record shortest cost to each node
- Pop cheapest, skip if visited, record dist, push neighbours
- Time O((V+E) log V), Space O(V+E)

**Network Delay Time (#743)**
- Standard Dijkstra from src to all nodes
- Return `max(dist.values())` if `len(dist) == n` else `-1`

**Cheapest Flights Within K Stops (#787)**
- Heap stores `(cost, stops, node)` — stops travel with the path
- No visited set — same node reachable via different stop counts
- `if node == dst: return cost` — first pop = cheapest valid path
- `if stops > k: continue` — prune dead paths

**Path With Minimum Effort (#1631)**
- Grid Dijkstra — heap stores `(effort, r, c)`
- `new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))`
- First time you pop destination = answer
- Time O(rows × cols × log(rows × cols))

## When to use what

| Signal in problem | Pattern |
|---|---|
| Sorted array + pair/target | Two Pointers |
| Subarray of size k | Sliding Window (fixed) |
| Longest substring | Sliding Window (dynamic) |
| Subarray sum = k | Prefix Sum + Hashmap |
| Sorted array + find/insert | Binary Search |
| Overlapping ranges | Merge Intervals |
| Tree level by level | BFS + deque |
| Tree path/depth | DFS recursion |
| Shortest path (unweighted) | BFS |
| Connected components / flood fill | DFS |
| Shortest path (weighted) | Dijkstra |
| Shortest path + constraint (k stops) | Dijkstra, no visited set, track in heap |
| kth largest / top k | Heap (size k) |
| Overlapping subproblems | Dynamic Programming |
| Linked list middle / cycle | Fast/Slow pointers |
| Linked list remove from end | Fast ahead by n, then both together |

## Useful Python patterns
- `enumerate(l)` → gives both index and value
- `defaultdict(list)` → dict with auto empty list
- `defaultdict(int)` → dict with auto 0
- `Counter(iterable)` → instant frequency dict
- `Counter.most_common(k)` → top k by frequency
- `sorted(dict, key=dict.get, reverse=True)` → sort by value
- `max(dict, key=dict.get)` → key with max value
- `"".join(sorted(word))` → sorted string (anagram key)
- `ord(c) - ord('a')` → letter to index (0-25)
- `nums[:k]` → first k elements
