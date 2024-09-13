class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return

            grid[r][c] = '0'

            dfs(r - 1, c)  # 上
            dfs(r + 1, c)  # 下
            dfs(r, c - 1)  # 左
            dfs(r, c + 1)  # 右

        num_islands = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    num_islands += 1
                
        return num_islands