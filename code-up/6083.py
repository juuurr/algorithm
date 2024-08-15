r, g, b = input().split()
r, g, b = int(r), int(g), int(b)

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            
print(r*g*b)
