from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Build graph and on-degree array
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Step 2: Initialize the queue with courses having no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        # Step 3: Process courses using BFS
        order = []
        while queue:
            course = queue.popleft()
            order.append(course) # Add course to the order

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if we processed all courses
        return order if len(order) == numCourses else []
        