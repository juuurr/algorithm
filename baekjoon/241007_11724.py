import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N)]
visited = [False]*N

for _ in range(M):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)


def bfs(m):
    dq = deque()
    dq.append(m)
    visited[m] = True #큐에 넣기 전에 방문 처리 -> 중복 방지 가능
    #동일한 노드가 중복해서 큐에 들어가지 않게 함
    #큐에 넣기 전에 방문처리 해야함!!!!

    while dq:
        x = dq.popleft()
        #visited[x] = True #큐에서 꺼낸 뒤 방문 처리
        #큐에 넣을때는 방문 처리를 하지 않으므로,
        #중복된 노드가 여러 번 큐에 들어갈 수 있음
        for node in adj[x]:
            if not visited[node]:
                visited[node] = True
                dq.append(node)


answer = 0
for i in range(N):
    if not visited[i]:
        bfs(i)
        answer += 1

print(answer)





#########################################
# 강의 풀이

# 1. 인접행렬 vs 인접 리스트
# 0 <= M <= N×(N-1)/2 ; nC2와 같음(자기자신으로 연결되는 간선이 없음)
# 간선 개수가 대각선 제외하고 모든 경우가 될 수 있으므로 인접 행렬이 낫겠다고 판단


# 2. dfs + 체크배열


# 인접행렬 + dfs
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
adj = [[0]*N for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: x-1, map(int, input().split()))
    adj[a][b] = adj[b][a] = 1

ans = 0
chk = [False]*N

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]: #now에서 nxt로 갈 수 있는 간선이 존재 하는 경우
            chk[nxt] = True
            dfs(nxt)

for i in range(N):
    if not chk[i]: #방문하지 않은 노드가 있다면
        ans += 1 #연결요소 추가
        chk[i] = True #방문처리
        dfs(i) #해당 노드와 연결된 모든 노드들을 bfs로 탐색 후 방문

print(ans)