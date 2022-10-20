"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# les copies sont mappés à leur parents pour qu'on puisse les accéder par après et faire
# les liens entre eux.
# les copies sont créés en visitant les voisins des nodes et non pas sur le cur node directement

class Solution:        
    def cloneGraph(self, node):

        if not node:
            return 

        # Crée copie premier node et la map
        nodeCopy = Node(node.val, [])
        dic = {node: nodeCopy}

        stack = [node]
        while stack:
            node = stack.pop()

            for neighbor in node.neighbors:
                
                # Si le node n'a pas été visité, on veut lui créer une copie et aussi l'ajouter
                # au stack pour pouvoir copier ses neighbors par après
                if neighbor not in dic:
                    
                    # Crée la copie du node et le map au node original
                    dic[neighbor] = Node(neighbor.val, [])
                    # L'ajouter au stack pour pouvoir visiter ses neighbors par après
                    stack.append(neighbor)

                # Fais le lien entre la copie du cur node et la copie du node parent
                dic[node].neighbors.append(dic[neighbor])
        
        # Retourne la copie du premier node 
        # (copie possède neighbors => connecte les copies ensemble)
        return nodeCopy