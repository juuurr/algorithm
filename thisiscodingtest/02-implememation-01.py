N = 5
plan = 'R R R U D D'.replace(' ', '') #공백 제거

#N = int(input())
#plan = input().split()
x, y = 1, 1 #초기값

for i in plan:
  if (i == 'L') and (0<y-1<N+1):
    y -= 1
  elif (i == 'R') and (0<y+1<N+1):
    y += 1
  elif (i == 'U') and (0<x-1<N+1):
    x -= 1
  elif (i == 'D') and (0<x+1<N+1):
    x += 1
print(x, y)



#책코드
#n = int(input())
#plans = input().split()

n = 5
plans = 'R R R U D D'.replace(' ', '') #공백 제거
x, y = 1, 1
#LRUD
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
types = ['L', 'R', 'U', 'D']

for plan in plans:
  for i in range(len(types)):
    if plan == types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if (nx < 1) or (ny < 1) or (nx > n) or (ny > n):
    continue  # 공간을 벗어나는 경우 무시
  else :
    x, y = nx, ny
print(x, y)