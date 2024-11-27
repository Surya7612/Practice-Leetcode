# import heapq
# from collections import defaultdict
# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         # Step 1: Build the graph
#         graph = defaultdict(list)
#         for u, v, w in flights:
#             graph[u].append((v, w))

#         # Step 2: Initialize the priority queue
#         pq = [[0, src, k+1]] # [[current_cost, current_node, stops_remaining]]

#         # Step 3: Process the priority queue
#         while pq:
#             curr_cost, node, stops = heapq.heappop(pq)

#             # if we reach the destination, return the cost
#             if node == dst:
#                 return curr_cost

#             # if we have stops remaining, process neighbors
#             if stops > 0:
#                 for neighbor, price in graph[node]:
#                     new_cost = curr_cost + price
#                     heapq.heappush(pq, (new_cost, neighbor, stops - 1))

#         # Step 4: If destination is not reachable
#         return -1

import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Step 1: Build the graph
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # Step 2: Initialize the priority queue and visited dictionary
        pq = [(0, src, k + 1)]  # (current_cost, current_node, stops_remaining)
        visited = {}  # (node, stops) -> cost
        
        # Step 3: Process the priority queue
        while pq:
            curr_cost, node, stops = heapq.heappop(pq)
            
            # If we reach the destination, return the cost
            if node == dst:
                return curr_cost
            
            # If we have stops remaining, process neighbors
            if stops > 0:
                for neighbor, price in graph[node]:
                    new_cost = curr_cost + price
                    if (neighbor, stops - 1) not in visited or new_cost < visited[(neighbor, stops - 1)]:
                        visited[(neighbor, stops - 1)] = new_cost
                        heapq.heappush(pq, (new_cost, neighbor, stops - 1))
        
        # Step 4: If destination is not reachable
        return -1
