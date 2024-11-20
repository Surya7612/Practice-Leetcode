class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if not grid:
        #     return 0

        # rows, cols = len(grid), len(grid[0])
        # num_islands = 0

        # def dfs(r,c):
        #     # Boundary and water checks
        #     if r < 0 or c < 0 or r >= rows or c >=cols or grid[r][c] == "0":
        #         return
        #     # Mark the cell visited
        #     grid[r][c] = "0"
        #     # Explore all directions
        #     dfs(r+1, c) # Down
        #     dfs(r-1, c) # Up
        #     dfs(r, c+1) # Right
        #     dfs(r, c-1) # Left

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1": # Found a new island
        #             num_islands += 1
        #             dfs(r,c)

        # return num_islands

        '''Now a BFS Solution'''

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def bfs(r,c):
            queue = deque([(r,c)])
            grid[r][c] = "0" # Mark as visited
            while queue:
                row, col = queue.popleft()
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = row + dr, col + dc
                    #Check boundaries and if cell is univisited land
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        grid[nr][nc] = "0" # Mark as visited

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1": # Found a new island
                    num_islands += 1
                    bfs(r,c)
            
        return num_islands


            
        