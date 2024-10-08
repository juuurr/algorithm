# BFS
# BFS 너비 우선 탐색이라는 이름에 걸맞게 그래프의 너비부터 탐색한다.
# DFS가 세로로 탐색하는 반면, BFS는 그래프를 가로로 탐색한다. 
# DFS는 인접 노드의 인접 노드를 계속해서 탐색해 가지만, 
# BFS는 인접 노드를 계속 큐에 넣어가며 큐에 들어온 순서대로 탐색을 시작하기에 시작 노드에서부터 가까운 노드들부터 탐색한다는 의미이다.

 

# 구체적인 동작 과정:

# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리.
# 2. 큐에서 노드를 꺼내 해당 노드의 방문하지 않은 모든 인접 노드를 모두 큐에 삽입하고 방문 처리.
# 3. 2번 과정을 더 이상 수행할 수 없을 때까지 반복.

import sys
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().split())
adj = [[] for _ in range(N)] #인접 리스트
visited = [False]*N

for _ in range(M):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)  # u에서 v로 연결
    adj[v-1].append(u-1)  # v에서 u로 연결 (무향 그래프이므로 양방향)


def bfs(start):
    queue = deque([start]) #큐 생성 후 큐에 시작 노드 삽입
    visited[start] = True #시작 노드를 방문 처리
    while queue:
        node = queue.popleft() #큐에서 노드를 꺼내 노드로 저장
        for neighbor in adj[node]: #인접 리스트 탐색
            if not visited[neighbor]: #방문하지 않은 노드가 있다면
                visited[neighbor] = True #방문 처리하고
                queue.append(neighbor) #큐에 넣어서 실제로도 방문


count = 0
for i in range(N):
    if not visited[i]:  # 방문하지 않은 노드 발견 시
        bfs(i)  # 그 노드로부터 BFS 수행
        count += 1  # 새로운 연결 요소 발견

print(count)
