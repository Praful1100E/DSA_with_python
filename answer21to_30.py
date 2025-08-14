# 21. Queue implementation using list
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)  # Add to end

    def dequeue(self):
        return self.queue.pop(0) if not self.is_empty() else None

    def is_empty(self):
        return len(self.queue) == 0


# 22. Find GCD of two numbers (Euclidean algorithm)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# 23. Check if number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 24. Reverse a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # Store next
        current.next = prev       # Reverse pointer
        prev = current            # Move prev forward
        current = next_node       # Move current forward
    return prev  # New head


# 25. BFS in a graph
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node] - visited)
    return visited


# 26. DFS in a graph
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start] - visited:
        dfs(graph, neighbor, visited)
    return visited


# 27. Find shortest path in unweighted graph (BFS)
def shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next_node in graph[vertex] - set(path):
            if next_node == end:
                return path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))
    return None


# 28. Find all permutations of a string
def string_permutations(s):
    if len(s) == 1:
        return [s]
    perms = []
    for i, char in enumerate(s):
        for perm in string_permutations(s[:i] + s[i+1:]):
            perms.append(char + perm)
    return perms


# 29. Knapsack Problem (0/1) - DP
def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]


# 30. Longest Common Subsequence (LCS) - DP
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]