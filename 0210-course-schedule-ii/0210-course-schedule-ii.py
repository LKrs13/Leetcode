class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        def buildAdjacencyList(n, edgesList):
            adjList = [[] for _ in range(n)]
            
            for c1, c2 in edgesList:
                adjList[c2].append(c1)
            
            return adjList
    
        def topoBFS(numNodes, edgesList):
            adjList = buildAdjacencyList(numNodes, edgesList)
    
            # number of incoming edges of each vertex
            inDegrees = [0] * numNodes
            for v1, v2 in edgesList:
                inDegrees[v1] += 1
            
            # all vertices with no incoming edge
            queue = []
            for v in range(numNodes):
                if inDegrees[v] == 0:
                    queue.append(v)
    
            # will contain the final topological order
            topoOrder = []
    
            while queue:
                v = queue.pop(0)
                topoOrder.append(v)
    
                # for each descendant of current vertex, reduce its in-degree by 1
                for des in adjList[v]:
                    inDegrees[des] -= 1

                    if inDegrees[des] == 0:
                        queue.append(des)
    
            return topoOrder
        
        res = topoBFS(numCourses, prerequisites)
        
        return res if len(res) == numCourses else []