import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Step 1: Sort courses by their deadline
        courses.sort(key=lambda x: x[1])
        
        # Step 2: Use a max heap to track durations of selected courses
        max_heap = []
        total_time = 0

        for duration, deadline in courses:
            heapq.heappush(max_heap, -duration) # Push the negative duration to simulate a max heap
            total_time += duration

            # If total time exceeds the deadline, remove the course with longest duration
            if total_time > deadline:
                total_time += heapq.heappop(max_heap)

        # The size of the heap gives the number of courses taken
        return len(max_heap)

        