#x, y = 1, 1 #좌우, 상하 #
#나이트 L (2, 1), ()
location = 'c2'
#location = input()
loc2num = location.translate(str.maketrans('abcdefgh','12345678'))
x, y = int(loc2num[0]), int(loc2num[1])

cnt = 0 #초기값

hor2 = [(2,1), (2,-1), (-2,1), (-2,-1)]
ver2 = [(1,2), (1,-2), (-1,2), (-1,-2)]

for h in hor2:
  (dx, dy) = h
  if (0 < x + dx < 9) and (0 < y + dy < 9):
    cnt += 1

for v in ver2:
  (dx, dy) = v
  if (0 < y + dy < 9) and (0 < x + dx < 9):
    cnt += 1

print(cnt)

#############################################################

cnt2 = 0 
ls = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
for i in ls :
  (dx, dy) = i
  if (0 < x + dx < 9) and (0 < y + dy < 9):
    cnt2 += 1

print(cnt2)