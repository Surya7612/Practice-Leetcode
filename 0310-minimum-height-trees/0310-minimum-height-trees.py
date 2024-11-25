
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Step 1: Handle edge cases
        if n <= 2:
            return [i for i in range(n)]

        # Step 2: Build the graph(adjacency list)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 3: Identify initial leaves
        leaves = deque([i for i in range(n) if len(graph[i]) == 1])

        # Step 4: Remove leaves iteratively
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count

            for _ in range(leaves_count):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)
                    if len(graph[neighbor]) == 1:
                        leaves.append(neighbor)

        # Step 5: Remaining nodes are the MHT roots
        return list(leaves)