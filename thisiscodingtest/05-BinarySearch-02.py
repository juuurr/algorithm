#떡볶이 떡 만들기
#떡의 길이가 일정하지 않음, 대신 한 봉지에 들어가는 떡의 총 길이는 일정
# 떡의 길이 < h(절단기 높이) -> 잘리지 않음
# 떡의 길이 > h(절단기 높이) -> 윗부분이 잘림
# 잘린 떡의 길이 만큼 손님이 가져감
# 손님 m만큼의 길이를 요청했을 떄,높이 h의 최댓값 구하기

n, m = 4, 6
rice = [19, 15, 10, 17]
rice = sorted(rice)
idx = len(rice)//2 - 1 #h보다 작은 수는 손님이 가져가지 않기 떄문에 

possible_h = [] #rice를 정렬했을 때 절반 기준으로 (15, 17) 가능한 h의 수 지정

for i in range(rice[idx], rice[idx+1]+1):
    possible_h.append(i)

possible_h = possible_h[::-1]

for h in possible_h :
    sum_ = 0 #초기값 설정
    for i in rice[idx:]:
        if i > h: #떡의 길이가 h보다 큰 경우만
            sum_ += i - h #손님이 가져가는 길이를 더해줌
    if sum_ == m:
        break

print(h)


#############################################################
# 이진 탐색 문제이자 파라메트릭 서치 유형의 문제
# 범위 내에서 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제면 이진 탐색으로 결정 문제를 해결
# 탐색 범위가 1부터 10억까지의 정수인데, 이처럼 큰 수를 보면 이진 탐색을 먼저 떠올리자!!!

######################### 코드 아이디에이션 #########################
# 0과 19 사이의 중간점을 h로 설정하기 !!

array = [19, 15, 10, 17]
sum_ = 0
n, m = 4, 6

# 1번 - 시작점은 0, 끝점은 가장 긴 떡의 길이 19로 설정
start = 0
end = max(array)
h = (start+end)//2
for num in array:
    if num - h > 0:
        sum_+= num - h
print(sum_)
#sum_ > m 이므로 시작점을 h+1로 옮김, sum_ 초기화
sum_ = 0
start = h + 1
end
h = (start+end)//2
h
for num in array:
    if num - h > 0:
        sum_+= num - h
print(sum_)

#sum_ > m 이므로 시작점을 h+1로 옮김, sum_ 초기화
sum_ = 0
start = h + 1
end
h = (start+end)//2
h
for num in array:
    if num - h > 0:
        sum_+= num - h
print(sum_)

#sum_ < m 이므로 끝점을 h-1로 옮김, sum_ 초기화
sum_ = 0
start
end = h - 1

h = (start+end)//2
h
for num in array:
    if num - h > 0:
        sum_+= num - h
print(sum_)

######################### 책 아이디에이션 기반 내 코드 #########################
n, m = 4, 6
array = [19, 15, 10, 17]

#초깃값 설정
sum_ = 0
start = 0
end = max(array)


while True :
    h = (start+end)//2

    for num in array:
        if num - h > 0:
            sum_ += num - h
    
    if sum_ > m :
        start = h + 1
    elif sum_ < m :
        end = h - 1
    else :
        break
    sum_ = 0 #초기화
print(h)


######################### 책 소스코드 #########################
n, m = 4, 6
array = [19, 15, 10, 17]

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행
result = 0
while (start <= end):
    total = 0 #sum_
    mid = (start+end)//2
    for x in array:
        if x > mid:
            total += x - mid
    
    if total < m : 
        end = mid - 1
    else :
        result = mid
        start = mid + 1
#초기화를 안하는데 왜 결과가 나오는거지? -> while문 처음에 초기화 !! total = 0
print(result)