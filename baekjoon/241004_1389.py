
from collections import deque

#인접 리스트
N, M = map(int, input().split())
adj = [[] for _ in range(N)]


for _ in range(M):
    u, v = map(int, input().rstrip().split())
    adj[u-1].append(v-1)
    adj[v-1].append(v-1)

N, M = 5, 5 #유저의 수 N
adj = [[2, 3], [1], [2, 2, 1], [3, 4, 2], [4]]



visited = [False] * N
def bfs(user):
    visited = [False] * N
    queue = deque([(user, user)])

    while queue:
        num, path = queue.popleft() #방문
        visited[num] = True #방문처리

        for nxt in adj[num]: #연결된 다음 사람의 idx
            if not visited[nxt]: #방문하지 않은 경우
                visited[nxt] = True #방문 처리 
                queue.append((nxt, path+nxt)) #직접 방문

    return(path)

ans = 0
for i in range(N):
    min()