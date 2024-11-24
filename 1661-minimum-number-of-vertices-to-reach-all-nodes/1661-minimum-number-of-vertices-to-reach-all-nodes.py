class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Step 1: Initialize in-degree array
        in_degree = [0] * n

        # Step 2: Populate in_degree for each node
        for _, to in edges:
            in_degree[to] += 1

        # Step 3: Collect nodes with in-degree 0
        result = [i for i in range(n) if in_degree[i] == 0]

        return result