import sys
input = sys.stdin.readline
S = set()

for i in range(int(input())):
    l = input().split()
    if len(l) == 2:
        cal, x = l[0], int(l[1])
        flag = x in S
    else:
        cal = l[0]

    if cal == 'all':
        S = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif cal == 'empty':
        S = set()
    elif cal == 'add':
        S.add(x)
    elif cal == 'remove':
        S.remove(x) if flag else S
    elif cal == 'check':
        print(1 if flag else 0)
    elif cal == 'toggle':
        S.remove(x) if flag else S.add(x)



#알고리즘 분류 - 비트마스킹