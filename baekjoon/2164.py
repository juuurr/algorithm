#1번 카드가 제일 위에, N번 카드가 제일 아래인 상태
#카드가 한 장 남을 때까지 다음 동작을 반복
#1. 제일 위에 있는 카드를 바닥에 버림
#2. 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮김

#N=4
#(선입)1234(후입)
#1회
#1번 -> 234 ; 선입선출
#2번 -> 342 ; 위치바꿈

#2회
#1번 -> 42 ; 선입선출
#2번 -> 24 ; 위치바꿈

#3회
#1번 -> 4 ; 선입선출


#선입선출 - Queue ; 삽입/삭제 - O(1)

from collections import deque

q = deque()

N = int(input())
for i in range(1, N+1):
    q.append(i)

while len(q) > 1:
    q.popleft() #선입선출
    q.append(q.popleft()) #위치바꿈

print(q.popleft()) #마지막 한 장의 카드 출력



##풀이 
#1번 - 삭제
#2번 - 삭제(맨 앞의 값) -> 삽입(맨 뒤로)
#배열에서 삭입/삭제 시간 복잡도 : O(N)
#N이 최대 500,000 -> 시간복잡도 :(N-1) * 3*O(N) -> O(N^2)
#-> 25*10^8 (1억에 1초인데 2초 제한이 있으므로)

#따라서 큐를 사용해야함

N = int(input())
dq = deque(range(1, N+1))

while len(q) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq.popleft())


#배열 풀이(시간초과)
N = int(input())
arr = [*range(1, N+1)]
while len(arr) > 1:
    arr.pop(0)
    arr.append(arr.pop(0))

print(arr.pop())