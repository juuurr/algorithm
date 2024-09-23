# 효율적인 화폐 구성 - 책 풀이
#N가지 종류의 화폐 - 최소한의 개수로 합이 M원이 되도록


#입력받기
coins = []
n, m = map(int, input().split())
for i in range(n):
    coins.append(int(input()))

coins = sorted(coins) #크기 순으로 정렬


dp = [0] + [10001]*(m) #m원(idx)을 만들기 위한 최소한의 화폐 개수. 0번 인덱스 제외


for i in range(1, m+1):
    for coin in coins:
        if dp[i-coin] != 10001: #(i-coin)원을 만드는 방법이 존재하는 경우
            dp[i] = min(dp[i], dp[i-coin]+1)


if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])