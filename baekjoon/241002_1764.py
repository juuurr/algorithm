N, M = map(int, input().split())

listen = set()
see = set()
ans = []
for _ in range(N):
    listen.add(input())
for _ in range(M):
    see.add(input())

#집합 자료형의 경우 이중 for문 탐색 - O(n+m)
lns = set.intersection(listen, see) #O(min(m, n))
ans = list(lns)
ans.sort()

print(len(ans))
for name in ans:
    print(name)


