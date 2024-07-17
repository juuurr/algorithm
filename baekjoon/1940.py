import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
num = list(map(int, input().split()))
num.sort()
 
#"두 수 ""의 합!!
cnt = 0 #만들 수 있는 갑옷 수
s_idx = 0 #start_index
e_idx = N-1 #fin_index


while s_idx < e_idx:
  if num[s_idx] + num[e_idx] == M:
    cnt += 1
    s_idx += 1
    e_idx -= 1
  elif num[s_idx] + num[e_idx] < M:
    s_idx += 1
  else:
    e_idx -= 1

print(cnt)



#시간 초과 코드
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
num = list(map(int, input().split()))
num.sort()
 
#"두 수 ""의 합!!
cnt = 0 #만들 수 있는 갑옷 수
s_idx = 0 #start_index
e_idx = N-1 #fin_index


while s_idx < e_idx:
  summ = num[s_idx] + num[e_idx]
  if summ == M: 
    cnt += 1
    s_idx += 1
    e_idx -= 1
  elif summ > M:
    pass
  else:
    s_idx += 1

print(cnt)