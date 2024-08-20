#음료수 얼려 먹기
#구멍이 뚫려 있는 부분끼리 상하좌우로 붙어 있는 경우 서로 연결된 것으로 간주

#0 == 구명이 뚫려있음
n, m = 4, 5
graph = [[0, 0, 1, 1, 0],
         [0, 0, 0, 1, 1],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0]]

#DFS 이용
#1. 특정 지점의 주변 상하좌우를 살핀 후 주변 지점 중 값이 0이면서 방문하지 않은 지점 방문
#2. 방문한 지점에서 다시 상하좌우를 살펴 방문을 다시 진행 -> 연결된 모든 지점 방문
#3. 반복

#graph : 그래프, v : 노드


n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#visited를 dfs함수로 구현
def dfs(x, y): #(0,0)
    if (x >= n) or (x < 0) or (y >= m) or (y < 0):
        return False
    if graph[x][y] == 0 : #아직 방문하지 않은 경우
        graph[x][y] = 1 #해당 노드 방문 처리

        dfs(x-1, y) #dfs(-1, 0) -> False
        dfs(x+1, y) #dfs(1, 0) -> dfs(0,0), dfs(2,0), dfs(1,-1), dfs(1,1) => True
                    #dfs(1,1) -> dfs(0,1), dfs(2,1), dfs(1,0), dfs(1,2)
                                #dfs(0,1) -> dfs(-1,1), (1,1), (0,0), (0,2)
                                                                #dfs(1,2) -> (0,2), (2,2), (1,1),(1,3)
                                                                #==> (1,1)=> True
        dfs(x, y-1) #(0,-1) -> False
        dfs(x, y+1) #(0,1) -> False

        return True #visited True로 -> return True
        #graph[x][y] == 0 인 경우는 무조건 True 반환
    
    return False #방문한 경우




#모든 노드에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)