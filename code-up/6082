#method 1
n = input()
lis = []
for i in range(1, int(n)+1):
    if (i <= 10) or (i == 20):
        if i%3 == 0:
            lis.append('X')
        else:
            lis.append(i)
    elif i < 30:
        if int(str(i)[-1])%3 == 0:
            lis.append('X')
        else:
            lis.append(i)

for j in range(len(lis)):
    print(lis[j], end = ' ')
    
    
    
    
#method 2

n = int(input())
for i in range(1, n+1):
    if (i%10==3) or (i%10 == 6) or (i%10 ==9):
        print("X", end=' ')
    else:
        print(i, end= ' ')
