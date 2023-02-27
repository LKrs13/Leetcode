from collections import defaultdict, deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        signals = {}
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        queue = deque([(k, 0)])
        while queue:
            node, cost = queue.popleft()
            if node not in signals or cost < signals[node]:
                signals[node] = cost
                for nextNode, nextCost in graph[node]:
                    queue.append((nextNode, cost + nextCost))

        if len(signals) != n:
            return -1
        
        return max(signals.values())