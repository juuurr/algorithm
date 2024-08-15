#grid 생성
d = []
for i in range(19):
    d.append([])
    for j in range(19):
        d[i].append(0)
        

#입력
for i in range(19):
    a = list(map(int, input().split()))
    for j in range(19):
        d[i][j] = a[j]



n = int(input())
inp = []
for i in range(n):
    xy = list(map(int, input().split()))
    inp.append(xy)
    



#십자 바꾸기
for k in range(n):
    for i in range(19):
        if d[i][inp[k][1]-1] == 0:
            d[i][inp[k][1]-1] = 1
        else:
            d[i][inp[k][1]-1] = 0
    
    for j in range(19):
        if d[inp[k][0]-1][j] == 0:
            d[inp[k][0]-1][j] = 1
        else:
            d[inp[k][0]-1][j] = 0
        

#출력
for i in range(19):
    for j in range(19):
        print(d[i][j], end = ' ')
    print()
