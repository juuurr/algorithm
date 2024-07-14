```
[합배열]
S[0] = A[0] # 초기화
S[i] = S[i-1] + A[i]

구간합 ; S[j]-S[i-1] ; i에서 j까지 구간 합
```

#방법1

#입력값 받기
N, M = map(int, input().split())
num_arr = list(map(int, input().split()))

idx_arr = []
for i in range(M):
  i, j = map(int, input().split())
  idx_arr.append((i-1,j-1))


#부분합 array 생성
sum_arr = [0 for i in range(N)] #공간 생성!!!!
for i in range(N):
  if i == 0:
    sum_arr[0] = num_arr[0]
  else:
    sum_arr[i] = sum_arr[i-1]+num_arr[i]


#i번째 수부터 j번째 수까지 합 출력
for idx in range(M):
  i = idx_arr[idx][0]
  j = idx_arr[idx][1]
  if i == j :
    print(num_arr[i])
  elif i == 0:
    print(sum_arr[j])
  else:
    print(sum_arr[j] - sum_arr[i-1])




#방법2
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_arr = list(map(int, input().split()))

sum_arr = [0] #index 조절
summ = 0 #초기값
for i in num_arr:
  summ += i
  sum_arr.append(summ)

#i,j 받고 출력
for m in range(M):
    i, j = map(int, input().split())
    print(sum_arr[j] - sum_arr[i-1])




