import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = []
for i in range(N):
    maze += input().split() #숫자로 받지 않았음 -> 1이 아니라 '1'!!


directions = [(-1,0), (1,0), (0, -1), (0, 1)]
visited = [[False]*M for _ in range(N)]

def bfs(n, m):
    q = deque([(n, m, [(n, m)])]) #입력 시 [(x,y)] 주의 !!!!!, 최단거리/길찾기 -> path
    visited[n][m] = True

    while q:
        x, y, path = q.popleft()

        if x == N-1 and y == M-1: #종료조건
            return len(path)

        for direction in directions:
            dx = x + direction[0]
            dy = y + direction[1]

            if 0 <= dx < N and 0 <= dy < M and not visited[dx][dy] and maze[dx][dy] == '1':
                visited[dx][dy] = True #방문처리
                q.append((dx, dy, path + [(dx, dy)]))


#bfs(0,0) #print하기!@@@@@@
print(bfs(0,0))


##########강의 풀이
#길찾기 문제(최단거리)
#칸을 셀 때 시작 위치와 도착 위치를 포함한다는 조건이 있음

#bfs는 최단거리 알고리즘 중 하나

from collections import deque

N, M = map(int, input().split())
board = [input() for _ in range(N)]
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def is_valid_coord(y, x): #범위 확인
    return 0 <= y < N and 0 <= x < M

def bfs():
    chk = [[False]*M for _ in range(N)]
    chk[0][0] = True

    dq = deque()
    #dq.append((0, 0))
    dq.append((0,0,1)) #몇칸 갔는지 count(시작점을 포함하기 때문에 처음은 1로 셈)

    while dq:
        y, x, d = dq.popleft()

        if y == N-1 and x == M-1:
            return d
        
        nxt_d  = d + 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = True
                dq.append((ny, nx, nxt_d))

print(bfs())