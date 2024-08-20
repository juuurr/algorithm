#1. 자료구조 기초

#탐색 : 많은 데이터 중에서 원하는 데이터를 찾는 과정 - DFS, BFS
#삽입(push), 삭제(pop)

#overflow ; 특정 자료구조가 수용할 수 있는 데이터 크기가 가득 찬 상태에서 삽입 연산 수행 시 발생
#underflow ; 특정한 자료구조에 데이터가 들어 있지 않은 상태에서 삭제 연산 수행 시 발생

#스택(stack) - 선입후출(first in last out), 후입선출(last in first out)
#파이썬에서 스택을 이용할 때는 별도의 라이브러리를 사용할 필요 없음
#기본 리스트에서 append()와 pop() 메서드를 이용하면 스택 자료구조와 동일하게 동작
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) #최하단 원소부터 출력
print(stack[::-1]) #최상단 원소부터 출력


#큐(Queue) - 선입선출(first in first out)
from collections import deque
#큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저 들어온 순서대로 출력
queue.reverse()
print(queue) #나중에 들어온 원소부터 출력


#재귀함수(recursive function) - 스택 자료구조 이용
#5-4
#재귀 함수 종료 조건
def recursive_function(i):
    if i == 10:
        return
    print(i, "번째 재귀 함수에서 ", i+1, "번째 재귀 함수를 호출합니다.")
    recursive_function(i+1)
    print(i, "번째 재귀 함수를 종료합니다.")
recursive_function(1)

#5-5
#2가지 방식으로 구현한 팩토리얼 예제
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n): #점화식, 반복문보다 간결
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

factorial_iterative(5)
factorial_recursive(5)


##########################################################

#2. 탐색 알고리즘 DFS/BFS
#2-1. DFS (Depth-First Search, 깊이 우선 탐색) ; 깊은 부분을 우선적으로 탐색

#그래프 : 노드(node)와 간선(edge)로 표현
#그래프 표현 방식 - 인접 행렬, 인접 리스트
#1) 인접 행렬(Adjacency Matrix) : 2차원 배열로 그래프의 연결 관계(각 노드가 연결된 형태)를 표현하는 방식
#연결이 되어 있지 않은 노드끼리는 무한(infinity)로 작성
#무한은 논리적으로 큰 값 999999999 등으로 초기화
#노드 개수가 많을수록 메모리가 불필요하게 낭비됨, 노드 연결 정보를 빠르게 얻을 수 없음

INF = 999999999 #무한의 비용 선언
#2차원 리스트를 이용해 인접 행렬 표현
graph = [[0, 7, 5],
         [7, 0, INF],
         [5, INF, 0]]
print(graph)

#2)인접 리스트(Adjacency List) : 리스트로 그래프의 연결 관게를 표현
#연결 리스트라는 자료구조를 이용해 구현 - 파이썬에서는 2차원 리스트 이용
#연결된 정보만을 저장하기 때문에 메모리 효율적 사용, 노드 연결 정보를 빠르게 얻을 수 있음
graph = [[] for _ in range(3)] #행이 3개인 2차원 리스트로 인접 리스트 표현

#노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append([2, 5])

#노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 7))

#노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0, 5))

print(graph)


#DFS의 동작 과정
#1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
#방문 처리 : 스택에 한 번 삽입되어 처리된 노드가 다시 삽입되지 않게 체크
#2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 함.
# 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다
#3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복
#일반적으로 인접한 노드 중에서 방문하지 않은 노드가 여러 개 있으면 번호가 낮은 순서부터 처리함



#DFS 메서드 정의
def dfs(graph, v, visited): 
    visited[v] = True #현재 노드를 방문 처리
    print(v, end = ' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph =[[], 
        [2, 3, 8], #노드1과 연결된 노드
        [1, 7], #노드2와 연결된 노드
        [1, 4, 5], #노드3과 연결된 노드
        [3, 5], #노드4와 연결된 노드
        [3, 4], #노드5와 연결된 노드
        [7], #노드6과 연결된 노드
        [2, 6, 8], #노드7과 연결된 노드
        [1, 7]] #노드8과 연결된 노드

visited = [False] * 9 #각 노드의 방문 정보를 리스트 자료형으로 표현(1차원 리스트)

dfs(graph, 1, visited)


#############################
#2-2. BFS(Breadth First Search, 너비 우선 탐색) ; 가까운 노드부터 탐색
#선입선출 방식인 큐 자료구조 이용
#O(N)의 시간이 소요됨, 일반적인 경우 DFS보다는 조금 더 빠르게 동작함

#BFS의 동작 과정
#1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
#2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 함
#(방문하지 않은 인접 노드가 없는 경우 무시, 따로 삽입하지 않고 다음 순서의 노드를 꺼냄)
#3. 2번의 과정을 반복
#인접 노드가 여러 개 있는 경우 숫자가 작은 노드부터 먼저 큐에 삽입


#라이브러리 임포트
from collections import deque

#BFS 메서드 정의
def bfs(graph, start, visited):
    #큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])

    #현재 노드를 방문 처리
    visited[start] = True

    #큐가 빌 때까지 반복
    while queue :
        #큐에서 원소 하나를 뽑아 출력
        v = queue.popleft()
        print(v, end = ' ')

        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i) #큐에 삽입
                visited[i] = True

#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph =[[], 
        [2, 3, 8], #노드1과 연결된 노드
        [1, 7], #노드2와 연결된 노드
        [1, 4, 5], #노드3과 연결된 노드
        [3, 5], #노드4와 연결된 노드
        [3, 4], #노드5와 연결된 노드
        [7], #노드6과 연결된 노드
        [2, 6, 8], #노드7과 연결된 노드
        [1, 7]] #노드8과 연결된 노드

visited = [False] * 9 #각 노드의 방문 정보를 리스트 자료형으로 표현(1차원 리스트)

bfs(graph, 1, visited)