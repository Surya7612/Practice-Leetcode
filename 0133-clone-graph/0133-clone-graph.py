"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS Approach
        if not node:
            return None

        # Map to store original node -> cloned node mapping
        cloned_nodes = {}

        # Recursive DFS function to clone the graph
        def dfs(curr_node):
            if curr_node in cloned_nodes:
                return cloned_nodes[curr_node]

            # Clone the current node
            clone = Node(curr_node.val)
            cloned_nodes[curr_node] = clone

            # Recursively clone all neighbors
            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)

        # BFS Approach
        # from collections import deque
        # ---
        # if not node:
        #     return None
        
        # # Map to store original node -> cloned node mapping
        # cloned_nodes = {node: Node(node.val)}
        
        # # BFS queue
        # queue = deque([node])
        
        # while queue:
        #     curr_node = queue.popleft()
            
        #     for neighbor in curr_node.neighbors:
        #         if neighbor not in cloned_nodes:
        #             # Clone the neighbor if not already cloned
        #             cloned_nodes[neighbor] = Node(neighbor.val)
        #             queue.append(neighbor)
                
        #         # Append the cloned neighbor to the current cloned node's neighbors
        #         cloned_nodes[curr_node].neighbors.append(cloned_nodes[neighbor])
        
        # return cloned_nodes[node]

