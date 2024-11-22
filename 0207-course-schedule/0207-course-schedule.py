from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Step 1: Build graph and in-degree array
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Step 2: Initialize queue with courses having no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        # Step 3: Process courses
        processed_courses = 0
        while queue:
            course = queue.popleft()
            processed_courses += 1

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                
        # Step 4: Check if all courses are processed
        return processed_courses == numCourses

        