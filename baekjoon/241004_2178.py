from collections import deque

N, M = map(int, input().split())
mapp = []
for _ in range(N):
    mapp.append(input().rstrip())


def bfs(n, m, count = 0): #시작점
    dq = deque([(n, m,[(n, m)])])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()

    while dq:
        x, y, path = dq.popleft() #path ; 방문 순서대로 노드를 저장

        if x == N-1 and y == M-1:
            return len(path)
        
        if mapp[x][y] == '1' and (x,y) not in visited:
            visited.add((x,y)) #방문 처리

        for direction in directions:
            dx = x + direction[0]
            dy = y + direction[1]

            if 0 <= dx < N and 0 <= dy < M and (dx, dy) not in visited:
                if mapp[dx][dy] == '1': #1인 경우에만 이동 가능
                    visited.add((dx, dy))
                    dq.append((dx, dy, path+[(dx, dy)]))


print(bfs(0,0))