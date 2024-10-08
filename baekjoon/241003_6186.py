import sys

input = sys.stdin.readline
R, C = map(int, input().split())

mapp = []
ans = 0
for _ in range(R):
    mapp.append(list(map(int, input().rstrip().replace('#', '1').replace('.', '0'))))

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
for x in range(R):
    for y in range(C):

        if mapp[x][y] == 1:
            ans += 1
            mapp[x][y] = 0 #방문으로 update

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < R and 0 <= ny < C and mapp[nx][ny] == 1:
                    mapp[nx][ny] = 0

print(ans)





#GPT풀이###############################################################################################
# Directions for moving up, down, left, right
import sys
input = sys.stdin.readline

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(grid, visited, r, c, R, C):
    # Stack-based DFS to mark all connected '#' symbols
    stack = [(r, c)]
    visited[r][c] = True
    while stack:
        x, y = stack.pop()
        # Explore all 4 possible directions (up, down, left, right)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check if the neighbor is within bounds and is a '#' that hasn't been visited
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and grid[nx][ny] == '#':
                visited[nx][ny] = True
                stack.append((nx, ny))

def count_grass_clumps(R, C, grid):
    # Visited matrix to track visited cells
    visited = [[False] * C for _ in range(R)]
    clump_count = 0
    
    # Iterate through each cell in the grid
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '#' and not visited[r][c]:
                # New clump found, perform DFS to mark the whole clump
                dfs(grid, visited, r, c, R, C)
                clump_count += 1
    
    return clump_count

# Input reading
R, C = map(int, input().split())
grid = [input().strip() for _ in range(R)]

# Output the number of grass clumps
print(count_grass_clumps(R, C, grid))