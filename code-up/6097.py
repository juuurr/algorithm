h, w = map(int, input().split())

grid = []
for i in range(int(h)):
    grid.append([])
    for j in range(int(w)):
        grid[i].append(0)

n = int(input())


for i in range(n):
    l,d,x,y = map(int, input().split())
    for j in range(l):
        if d == 0:
            grid[x-1][y + j -1] = 1
        elif d == 1:
            grid[x+j-1][y-1] = 1


for i in range(h):
    for j in range(w):
        print(grid[i][j], end = ' ')
    print()
