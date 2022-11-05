class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # calculate the amount of times we need to connect components together
        
        # parents of each node
        par = [i for i in range(n)]

        # number of nodes connected to each node (root)
        rank = [1] * (n) 
        
        # finding highest parent of n
        def find(n):

            # get parent of node
            p = par[n]
            
            while p != par[p]:
                # path compression: setting parent to great parent
                par[p] = par[par[p]]
                
                p = par[p]
            
            return p
    
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            # if share same parent => already connected
            if p1 == p2:
                return False
            
            # add node to parent with highest rank & update rank
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True
        
        ct = n
        
        for n1, n2 in edges:
            if union(n1, n2):
                ct -= 1
                
        return ct
        