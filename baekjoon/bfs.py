#https://velog.io/@sihoon_cho/Python코딩테스트-코딩테스트-완전정복-BFS-너비우선탐색
#https://data-marketing-bk.tistory.com/entry/BFS-%EC%99%84%EB%B2%BD-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

#"방문하고자 하는 노드"와 "방문했던 노드"를 나누어서 알고리즘 구성하는 것이 핵심
#bfs ; 기본순회, 최단경로, 연결요소(현재 노드 기준 연결된 모든 노드 탐색), 플러드 필 문제(땅따먹기)

# BFS 과정에서 deque 활용

# 	1.	큐 초기화: 시작 노드를 큐에 넣습니다.
# 	2.	큐에서 노드 꺼내기: 큐에서 가장 먼저 들어간 노드를 꺼내어 현재 노드로 설정합니다.
# 	3.	인접한 노드들 탐색: 현재 노드의 인접 노드를 모두 방문하고, 방문한 노드를 큐에 추가합니다.
# 	4.	반복: 큐가 비어 있을 때까지 2번과 3번 과정을 반복합니다.

#graph가 주어지는 형식
#1. graph가 dictionary일 때 BFS
#단방향그래프
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

from collections import deque

def bfs(start_node, graph):
    dq = deque([start_node])
    visited = set([start_node]) #set의 경우 하나의 덩어리로 넣어야 함

    while dq: #dq가 비어있지 않는 경우
        curr_node = dq.popleft() #현재 노드 위치

        for next_node in graph[curr_node]: #현재 노드와 연결된 노드들
            if next_node not in visited: #다음 노드들을 방문하지 않은 경우
                visited.add(next_node)
                dq.append(next_node)


