#게임 개발

#n, e, s, w = 0, 1, 2, 3 #북, 동, 남, 서
n, m = map(int, input().split())
game = [] #빈 공간 생성
x, y, d = map(int, input().split())
for i in range(n):
    game.append(list(map(int, input().split())))


way = [(-1, 0), (0, 1), (1, 0), (0, -1)] #북, 동, 남, 서 

#처음 방문
cnt = 1
game[x][y] = 1 # 방문한 칸 업데이트

d_cnt = 0

while True:
    d -= 1
    if d < 0 :
        d += 4
    dx, dy = way[d][0], way[d][1]
    if game[x+dx][y+dy] == 0 :
        game[x+dx][y+dy] = 1 #가본 길로 업데이트
        cnt += 1 #방문한 칸 업데이트
        x, y = x+dx, y+dy #유저 위치 업데이트
        d_cnt = 0 #초기화
    else :
        d_cnt += 1
    if d_cnt == 4: #4방향 모두 돈 경우
        x, y = x-dx, y-dy
        if game[x-dx][y-dy] == 1:
            break




#######################아이디에이션##############################
#(N, M)칸 육지 or 바다 -> 캐릭터는 바다로 갈 수 없음
#캐릭터 - 동서남북
#(A, B) - (북쪽으로 떨어진 칸의 개수, 서쪽으로 떨어진 칸의 개수)

#1. 왼쪽방향부터 갈곳 정하기
#2. if 왼쪽 방향이 안가본 길 - 왼쪽 방향으로 회전, 왼쪽 한칸 전진
# else(가본길 or 바다) - 왼쪽방향으로 회전 후 1단계 
#3. 네 방향 모두 가본 칸이거나 바다 - 바라보는 방향 유지한 채로 한칸 뒤로 가고 1단계로 이동
# if 뒤쪽방향이 바다 - 움직임 멈추기

n, m = 4, 4 # n, m = map(int, input().split())
x, y, d = 1, 1, 0 #x, y, d = map(int, input().split())

game = [[1,1,1,1], [1,0,0,1], [1,1,0,1],[1,1,1,1]]

# 1 - 현재 방향 기준으로 왼쪽 
d = 3 # d-1


# 2 - 왼쪽 방향이 바다임을 판단
dx, dy = way[d][0], way[d][1]
print(game[x+dx][y+dy]) # == 1

# 1 - 현재 방향 기준으로 왼쪽
d = 2

# 2
dx, dy = way[d][0], way[d][1]
print(game[x+dx][y+dy])
print(x+dx, y+dy)


# 1
d = 1
#2
dx, dy = way[d][0], way[d][1]
print(game[x+dx][y+dy]) # == 0
print(x+dx, y+dy)

game[x+dx][y+dy] = 1 #가본 길로 업데이트
cnt += 1 #방문한 칸 업데이트
x, y = x+dx, y+dy #유저 위치 업데이트

##########################

d = 0
dx, dy = way[d][0], way[d][1]
print(game[x+dx][y+dy]) # == 1
print(x+dx, y+dy)

d = 3

d = 2
dx, dy = way[d][0], way[d][1]
print(game[x+dx][y+dy]) 
game[x+dx][y+dy] = 1 #가본 길로 업데이트
cnt += 1 #방문한 칸 업데이트
x, y = x+dx, y+dy #유저 위치 업데이트

print(x,y)

########################
d = 1
dx, dy = way[d][0], way[d][1]
print(game[x+dx][y+dy]) 

d = 0
dx, dy = way[d][0], way[d][1]
print(game[x+dx][y+dy]) 

d = 3
dx, dy = way[d][0], way[d][1]
print(game[x+dx][y+dy]) 

d = 2
dx, dy = way[d][0], way[d][1]
print(game[x+dx][y+dy]) 
print(x,y)
#방향을 유지한 채 한칸 뒤로
print(x-dx, y-dy) #뒤로 이동

game[x-dx][y-dy] #1이면 stop #2이면 x,y 위치 업데이트