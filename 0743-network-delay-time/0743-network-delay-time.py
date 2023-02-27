from collections import defaultdict, deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        signals = defaultdict(lambda: float('inf'))
        signals[k] = 0
        visited = set()
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        queue = deque([(k, 0)])
        while queue:
            node, cost = queue.popleft()
            for nextNode, nextCost in graph[node]:
                signals[nextNode] = min(signals[nextNode], cost + nextCost)
                if (node, nextNode, signals[nextNode]) in visited:
                    continue
                visited.add((node, nextNode, signals[nextNode]))
                queue.append((nextNode, signals[nextNode]))
        
        if len(signals) != n:
            return -1
        
        return max(signals.values())