import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Step 1: Build the graph (adjacency list)
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Step 2: Initialize distances and priority queue
        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[k] = 0
        pq = [(0, k)] # (current_time, node)

        # Step 3: Process the priority queue
        while pq:
            curr_time, node = heapq.heappop(pq)

            # Skip if the current time is worse than the known distance
            if curr_time > distances[node]:
                continue

            for neighbor, weight in graph[node]:
                new_time = curr_time + weight
                if new_time < distances[neighbor]:
                    distances[neighbor] = new_time
                    heapq.heappush(pq, (new_time, neighbor))

        # Step 4: Get the maximum distance
        max_time = max(distances.values())
        return max_time if max_time < float('inf') else -1        