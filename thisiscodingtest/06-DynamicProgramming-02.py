# 개미 전사
#최소 한 칸 이상 떨어진 식량창고를 약탈해 최대한 많은 식량을 얻는 것이 목표

n = 4 #int(input())
array = [1,3,1,5] #list(map(int, input().split()))
dp = [0]*n

dp[0] = array[0]
dp[1] = max(array[0], array[1]) #global 합계!!

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+array[i])
    #직전 값(i-1)의 global 최댓값과
    #한칸 뛴 값(i-2)과 현재 값(i)의 합을 비교해서 큰 값을 새로운 global max로 저장

print(dp[n-1])


#############################################################
# 내 풀이 (잘못된 풀이)
#문제1) dp에 global하게 합계가 큰 것만 저장해야 되는데 locally 생각함
n = 4 #int(input())
array = [1,3,1,5] #list(map(int, input().split()))
dp = [0]*n

dp[0] = array[0] #1
dp[1] = array[1] #3 -> global 합계 고려 x. 특정 상황에만 맞음
dp[2] = dp[0]+array[2] #1+1
if n > 3:
    dp[3] = dp[1]+array[3] #3+5
    for i in range(4, n):
        dp[i] = max(dp[i-2], dp[i-3]) + array[i]
        #문제2) 이렇게 하면 최소 한칸만 띄우라는 조건에 맞지 않음
print(max(dp)) #문제3) 추가적인 시간 소요 <- 문제1을 고려하지 못해서 발생


#############################################################
#아이디에이션

#무조건 한칸만 건너뛰면 되지 않나...??
#최소 한칸 이상인데 한 칸 초과로 뛰어서 최적해를 찾을 수 있는지 모르겠음
array = [1, 3, 1, 5, 10, 11, 12, 1, 3] #출력 28
print(1+1+10+12+3) #한칸만 건너뛴 경우 최적해 x
print(3+10+12+3) #최적해

n = len(array)
dp = [0] * (n-1)



dp[0] = array[0] #1
dp[1] = array[1] #3
dp[2] = dp[0]+array[2] #1+1
dp[3] = dp[1]+array[3] #3+5
# 지금까지    dp : [1, 3, 2, 8, 0, 0, 0, 0]
# 지금까지 array : [-, -, -, -, 10, 11, 12, 1, 3]

dp[4] = max(dp[1], dp[2]) + array[4]
# 지금까지    dp : [1, 3, 2, 8, 13, 0, 0, 0]
# 지금까지 array : [-, -, -, -, -, 11, 12, 1, 3]

dp[5] = max(dp[2], dp[3]) + array[5]


