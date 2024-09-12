#1로 만들기
#참고자료
# https://velog.io/@qtly_u/DP-백준-1463번-1로-만들기
# https://jae04099.tistory.com/199
# https://hongcoding.tistory.com/46

X = 26

# X = 26인 경우
# 26 -> 25 -> 5 -> 1 과정을 거쳐 1이 되게 됨
# X = 25인 경우에는 25 -> 5 -> 1의 과정을,
# X = 5인 경우에는 5 -> 1의 과정을 거침

#즉, 26을 구할 떄는 25의 결과를, 25를 구할 때는 5의 결과를 이용
# 앞에서 구한 결과값을 저장하였다가 후에 사용!!
# ==> 제일 작은 수부터 미리 계산된 값을 저장해두고 필요할 때 빼서 쓰기 !
# 그래서 DP를 사용할 수 있음

#1을 빼기, 2로 나누기, 3으로 나누기, 5로 나누기 -> 모든 연산을 수행해서
#해당 단계에서 제일 숫자를 작게하는 연산 횟수를 저장해야 함


dp = [0] * (X+1)
#dp 테이블에 연산 횟수를 저장함
#X+1이라고 한 이유는 0번 인덱스를 사용하지 않고, 1번 인덱스를 첫 번째 수로 인식하기 위해서


for i in range(2, X+1): #2부터 시작하는 이유는 dp[1]은 항상 0이기 떄문(X=1이면 연산 0번 수행)
    dp[i] = dp[i-1] + 1 #1빼는 연산 수행, 연산 횟수를 +1로 저장

    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5]+1)
        #dp[i]에 1을 더하지 않는 것은 위에 1빼는 연산 수행하며 +1을 추가했기 때문
        #dp[i//5]의 연산에 i%5 연산을 1회 더했으므로 d[i//5]+1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    
    #min으로 dp[i]와 dp[i//n]+1을 비교해서 작은 수를 저장!!

print(dp[X])