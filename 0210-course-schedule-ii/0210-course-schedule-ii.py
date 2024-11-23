from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # # Step 1: Build graph and on-degree array
        # graph = defaultdict(list)
        # in_degree = [0] * numCourses

        # for course, prereq in prerequisites:
        #     graph[prereq].append(course)
        #     in_degree[course] += 1

        # # Step 2: Initialize the queue with courses having no prerequisites
        # queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        # # Step 3: Process courses using BFS
        # order = []
        # while queue:
        #     course = queue.popleft()
        #     order.append(course) # Add course to the order

        #     for neighbor in graph[course]:
        #         in_degree[neighbor] -= 1
        #         if in_degree[neighbor] == 0:
        #             queue.append(neighbor)

        # # Step 4: Check if we processed all courses
        # return order if len(order) == numCourses else []
        '''Now Using DFS'''
        # Step 1: Build Graph
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            
        # Step 2: Initialize visited array and order list
        visited = [0] * numCourses
        order = []
        cycle_detected = False

        # Step 3: Define DFS
        def dfs(course):
            nonlocal cycle_detected # allows the function to modify the outer cycle_detected variable
            if visited[course] == 1: # Cycle detected
                cycle_detected = True
                return
            if visited[course] == 2: # Already processed
                return

            visited[course] = 1 # Mark as visiting
            for neighbor in graph[course]:
                dfs(neighbor)
                if cycle_detected:
                    return
            visited[course] = 2 # Mark as Processes
            order.append(course) # Post-Order add

        # Step 4: Perform DFS for all courses
        for course in range(numCourses):
            if visited[course] == 0:
                dfs(course)
                if cycle_detected:
                    return []
        
        return order[::-1] # Reverse post-order for topological order

        