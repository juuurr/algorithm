N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]
count = 0

visited = [[False]*M for _ in range(N)]
directions = [(1, 0), (0, 1)]


def bfs(grid, n, m):

    stack = [(n,m)] #현재 위치
    visited[n][m] = True #방문 처리

    while stack:
        x, y = stack.pop()
        for direction in directions:
            dx, dy = x + direction[0], y + direction[1]

            if 0 <= dx < N and 0 <= dy < M and grid[dx][dy] == '*' and not visited[dx][dy]:
                visited[dx][dy] = True
                stack.append((dx, dy))

for n in range(N):
    for m in range(M):
        if grid[n][m] == '*' and not visited[n][m]:
            bfs(grid, n, m)
            count += 1


print(count)
