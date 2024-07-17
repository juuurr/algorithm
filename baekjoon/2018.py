#책 코드
n = int(input())
cnt, s, e, now_sum = 1, 1, 1, 1

while e != n:
  if now_sum == n :
    cnt += 1
    e += 1
    now_sum += e
  elif now_sum > n :
    now_sum -= s #start 포인터 이동
    s += 1
  else:
    e += 1
    now_sum += e #end 포인터 이동

print(cnt)


#메모리초과 코드
import sys
N = int(sys.stdin.readline())
#N = 15
num_arr = [i for i in range(1, N+1)]

s, e, cnt = 0, 0, 0 #시작 인덱스, 끝 인덱스, 방법 수
now_sum = 0 #현재 포인터 위치의 합

for s in range(N): #시작점을 하나씩 움직임
  e = s #끝 점을 처음 점으로 초기화
  while now_sum < N and e < N:
    now_sum += num_arr[e]
    e += 1
  if now_sum == N:
    cnt += 1
  now_sum = 0 #초기화
print(cnt)


#시간초과 코드

# 연속된 자연수이므로 (인덱스 번호+1) == 해당 인덱스의 원소!!
# 따라서 리스트를 만들 필요가 전혀 없음

import sys
N = int(sys.stdin.readline())

s, e, now_sum, cnt = 1, 1, 1, 1 #시작 인덱스, 끝 인덱스, 방법 수


while e != N:
  if now_sum == N :
    cnt += 1
    s += 1
    e = s
    now_sum = s
  elif now_sum < N :
    e += 1
    now_sum += e
  else :
    s += 1
    now_sum = s
    e = s

print(cnt)
