import sys
from collections import deque

input = sys.stdin.readline
N, M, V = map(int, input().split())

adj = [[0]*N for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    adj[x-1][y-1] = 1
    adj[y-1][x-1] = 1




########################################################dfs
chk_dfs = [False]*N
dfs_ans = []

def dfs(now):
    for nxt in range(N): #인접 노드 방문, node 개수
        if adj[now][nxt] == 1 and not chk_dfs[nxt]:
            dfs_ans.append(nxt+1) #방문한 노드 기록
            chk_dfs[nxt] = True #방문처리
            dfs(nxt)
            
dfs_ans.append(V) #탐색 시작점을 방문한 노드에 기록
chk_dfs[V-1] = True #방문 처리
dfs(V-1)


########################################################bfs
chk_bfs = [False]*N
bfs_ans = []

def bfs(node):
    q = deque([node])
    chk_bfs[node] = True #방문 처리

    while q:
        now = q.popleft()
        for nxt in range(N):
            if adj[now][nxt] == 1 and not chk_bfs[nxt]:
                bfs_ans.append(nxt+1) #방문 기록
                chk_bfs[nxt] = True #방문처리
                q.append(nxt)


bfs_ans.append(V)
bfs(V-1)

########################################################출력
print(" ".join(map(str, dfs_ans)))
print(" ".join(map(str, bfs_ans)))