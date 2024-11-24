class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ''' Using Union-Find(Disjoint Set Union)
        1. Each node starts at its own parent (root)
        2. Use union to connect the nodes.
        3. Use find to determine the root of a node.
        - If two nodes are already connected(share the same root), adding their edge forms a cycle.
        Steps:
            Initialize a parent array to track roots.
            For each edge, check:
            - If the two nodes are already connected, the edge is redundant.
            - Otherwise, connect them using union.
        '''

        # Step 1: Initilaize parent array and rank array
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        # Step 2: Define find and union functions
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])  # Path compression
            return parent[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            if root1 == root2:
                return False # Cycle detected
            
            # Union by rank
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
            
            return True

        # Step 3: Process edges
        for u,v in edges:
            if not union(u,v):
                return [u,v] # Return the edge that forms a cycle