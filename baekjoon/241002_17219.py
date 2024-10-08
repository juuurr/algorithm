import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dic = {}
for _ in range(N):
    url, password = input().split()
    dic[url] = password

for _ in range(M):
    print(dic[input().rstrip()])