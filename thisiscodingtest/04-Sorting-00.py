#정렬(Sorting) : 데이터를 특정한 기준에 따라서 순서대로 나열
#데이터 정렬 후 이진 탐색이 가능해짐

#예제 : 7, 5, 9, 0, 3, 1, 6, 2, 4, 8을 오름차순으로 정렬
#내림차순의 경우 리스트 뒤집는 Reverse 연산으로 수행 가능(시간 복잡도 - O(N))

############################

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
    for j in range(i+1, len(array)): #다음 원소부터 탐색
        if array[min_index] > array[j]:
            min_index = j #가장 작은 원소의 인덱스