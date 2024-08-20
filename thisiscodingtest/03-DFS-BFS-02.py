#미로 탈출

n, m = 5, 6
graph = [[1, 0, 1, 0, 1, 0],
         [1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1]]
#괴물이 없는 부분은 1 -> 1로만 가야함

#bfs : 시작 지점에서 가까운 노드부터 차례로 그래프의 모든 노드 탐색

from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (nx >= n) or (nx < 0) or (ny >= m) or (ny < 0):
                continue
            
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,  ny))

    return graph[n-1][m-1]

print(bfs(0,0))