class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        queue = deque([(0, k)])
        visited = {}
        while queue:
            t, u = queue.popleft()
            if u not in visited or t < visited[u]:
                visited[u] = t
                for v, w in graph[u]:
                    queue.append((t + w, v))
        return -1 if len(visited) < n else max(visited.values())