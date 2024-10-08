import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # Convert both inputs to integers
coins = [int(input()) for _ in range(N)]

coins.sort(reverse = True)
cnt = 0
for coin in coins:
    if K % coin < K:
        cnt += K // coin
        K -= (K//coin)*coin
    if K == 0:
        break

print(cnt)


#############################################강의 해설
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()
ans = 0
for coin in coins:
    ans += K // coin
    K %= coin

print(ans)