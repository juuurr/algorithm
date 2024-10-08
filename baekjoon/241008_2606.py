#1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력
from collections import deque

n = int(input()) #정점(노드) 개수 - 100이하인 양의 정수. 1번부터
e = int(input()) #간선 개수


adj = [[0]* n for _ in range(n)]
visited = [False] * n

for i in range(e):
    x, y = map(int, input().split())
    adj[x-1][y-1] = 1
    adj[y-1][x-1] = 1

root = [] #방문한 노드 기록
def bfs(node = 0):
    dq = deque([node])
    visited[node] = True

    while dq:
        now = dq.popleft()
        for nxt in range(n):
            if not visited[nxt] and adj[now][nxt] == 1:
                root.append(nxt)
                visited[nxt] = True
                dq.append(nxt)
    return len(root)


print(bfs(0))