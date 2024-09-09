#정렬(Sorting) : 데이터를 특정한 기준에 따라서 순서대로 나열
#데이터 정렬 후 이진 탐색이 가능해짐

#예제 : 7, 5, 9, 0, 3, 1, 6, 2, 4, 8을 오름차순으로 정렬
#내림차순의 경우 리스트 뒤집는 Reverse 연산으로 수행 가능(시간 복잡도 - O(N))

####################################################################################

#1. 선택정렬 Selection Sort
# 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 두 번째 데이터와 바꿈
# => 정렬되지 않은 데이터 중 가장 작은 데이터를 앞으로 보내는 과정을 N-1번 반복하면 정렬이 완료됨

#1-1) 소스코드
#스와프(Swap) : 특정한 리스트가 주어졌을 때 두 변수의 위치를 변경하는 작업

#파이썬 스와프 코드
array1 = [3, 5]
array1[0], array1[1] = array1[1], array1[0]
print(array1)


#내 구현 코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array) - 1): #마지막 요소는 비교할 필요가 없음
    min_val = min(array[i+1:]) #자기 자신 제외하고 최솟값 탐색
    min_idx = array.index(min_val)
    array[i], array[min_idx] = array[min_idx], array[i]
print(array)

# 책 구현 코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)): #min_index의 다음 원소부터 끝까지 최솟값 탐색
        if array[min_index] > array[j]:
            min_index = j #가장 작은 원소의 인덱스로 update
    array[i], array[min_index] = array[min_index], array[i]
print(array)

#1-2) 선택 정렬의 시간복잡도 : O(N^2)


####################################################################################
#2. 삽입 정렬 Insertion Sort
# 데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입
# 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정함
# 삽입 정렬의 경우, 첫 번째 데이터는 그 자체로 정렬되어 있다고 판단하기 때무에 두 번째 데이터부터 정렬을 시작함
# 정렬이 이루어진 원소는 항상 오름차순 -> 특정 데이터가 삽입될 위치를 선정할 때, 삽입될 데이터보다 작은 데이터를 만나면 그 위치에서 멈추기

#2-1) 소스코드
#내 구현 코드
# insert(a, b)는 리스트의 a번째 위치에 b를 삽입하는 함수
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(array)) :
    for j in range(0, i):
        if array[i] < array[j]:
            i_val = array.pop(i)
            array.insert(j, i_val)
        else:
            break
print(array)


#책 구현 코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]: #뒤에서부터 탐색, 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else: #자기 보다 작은 데이터를 만나면 for문 탈출
            break
print(array)

#2-2) 시간복잡도 : O(N^2), 거의 정렬이 되어있는 최선의 경우, O(N)의 시간 복잡도를 가짐
# 보통의 경우 퀵 정렬 알고리즘보다 비효율적이나, 정렬이 거의 되어 있는 경우에는 퀵 정렬보다 빠름


####################################################################################
#3. 퀵 정렬 Quick Sort (가장 많이 사용됨)
#기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸기
#기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작
#기준 == pivot -> 피벗 구하는 방법이 여러 가지인데, 책에서는 호어 분할(hoare partition) 방식
#호어분할 : 리스트에서 첫 번째 데이터를 피벗으로 정함
#피벗 설정 후, 왼쪽에서 피벗보다 큰 데이터를 찾고 오른쪽에서 피벗보다 작은 데이터를 찾고 서로 교환
#찾는 위치가 엇갈린 경우 작은 데이터와 피벗의 위치를 서로 변경함
#피벗을 설정하여 정렬을 수행한 후에 피벗을 기준으로 왼쪽 리스트와 오른쪽 리스트에서 각각 다시 정렬 수행
#재귀 함수로 구현 시 간결해짐
#퀵 정렬 종료 조건 - 현재 리스트의 데이터 개수가 1개인 경우

#3-1) 소스코드
# 내 구현 코드 + 책 구현 코드1

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot_idx = start
    pivot = array[pivot_idx]
    left_idx = start + 1
    right_idx = end

    while left_idx <= right_idx:
        while (left_idx <= end) and (array[left_idx] < pivot):
            left_idx += 1
            
        while (right_idx > start) and (array[right_idx] > pivot):
            right_idx -= 1
        
        if left_idx <= right_idx: #엇갈리지 않은 경우
            array[left_idx], array[right_idx] = array[right_idx], array[left_idx]
        
        else: #엇갈린 경우
            array[right_idx], array[pivot_idx] = array[pivot_idx],array[right_idx]
            pivot_idx = right_idx
    
    quick_sort(array, start, pivot_idx-1)
    quick_sort(array, pivot_idx+1, end)

quick_sort(array, 0, len(array) - 1)
print(array)


# 책 구현 코드2
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort2(array):
    if len(array) <= 1 : #리스트가 하나 이하의 원소만 담고 있다면 종료
        return array
    
    pivot = array[0] #피봇은 첫 번째 원소
    tail = array[1:] #피벗을 제외한 원소

    left_side = [x for x in tail if x <= pivot] #분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

print(quick_sort2(array))

#3-2) 시간복잡도 : 평균적으로 O(NlogN), 최악의 경우 O(N^2)
#삽입 정렬은 이미 데이터가 정렬되어 있는 경우 빠르게 동작, 


####################################################################################
#4. 계수 정렬 Count Sort
# 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
# 특정한 조건 == 데이터의 크기 범위(max-min < 1000000)가 제한되어 정수 형태로 표현할 수 있을 떄
# 계수 정렬은 직접 데이터의 값을 비교한 뒤에 위치를 변경하며 정렬하는 방식(비교 기반의 정렬 알고리즘)이 아님
# 일반적으로 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담는다는 특징이 있음

# 개념
# 초기단계
#리스트의 인덱스가 모든 범위(0부터 9까지)를 포함할 수 있도록 설정


# 1.
#4-1) 소스코드
# 내 구현 코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0 for _ in range(max(array)+1)]

for num in array:
    count[num] += 1

for idx in range(len(count)):
    for c in range(count[idx]):
        print(idx, end = ' ')


# 책 구현 코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * (max(array)+1)
for i in range(len(array)):
    count[array[i]] += 1
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end =' ')

#4-2) 시간복잡도 : O(N+K) ; 모든 데이터가 양의 정수인 상황에서 데이터의 개수를 N, 데이터 중 최댓값의 크기를 K
#기수정렬과 계수정렬이 제일 빠름
# 기수 정렬은 계수 정렬에 비해 동작은 느리지만 처리할 수 있는 정수의 크기는 더 큼
# 공간 복잡도 고려, 계수 정렬은 동일한 값을 가지는 데이터가 여러 개 등장할 떄 적합함
# 퀵 정렬은 일반적인 경우에 평균적으로 빠르게 동작하므로 데이터의 특성을 파악하기 어려우면 퀵 정렬을 이용하는 것이 유리


####################################################################################
#파이썬의 정렬 알고리즘
#sorted() : 최악의 경우 시간 복잡도 O(NlogN)
#sort()
#key 매개변수를 입력으로 받을 수 있고, key는 하나의 함수가 들어가야 하며 이는 정렬의 기준이 됨
array = [('바나나', 2), ('사과', 5), ('당근', 3)]
result = sorted(array, key = lambda x : x[1])
result