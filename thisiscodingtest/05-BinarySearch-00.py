#<범위를 반씩 좁혀가는 탐색>
#1. 순차 탐색(Sequential Search) : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 차례대로 확인
#사례 - 리스트에 특정 값의 원소가 있는지 체크, 리스트에서 특정 값을 가지는 원소의 개수를 세는 count() 메서드의 내부

def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1 #찾는 원소의 인덱스 반환
#시간 복잡도 : 최악의 경우 O(N)

####################################################################################
#2. 이진 탐색(Binary Search) : 반으로 쪼개면서 탐색하기
#위치 변수 3개 이용 - 범위의 시작점, 끝점, 중간점 -> 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교
#시간 복잡도 : O(logN)
#내 풀이
import math
n, target = 10, 7
array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

def jr_binary_search(n, target, array):
    start = 0
    end = n-1 #인덱스 번호
    middle = math.floor((start+end)/2)

    while array[middle] != target: #값이 없는 경우 무한 루프 발생.. !!!
        middle = math.floor((start+end)/2)
        if array[middle] > target: # 8 > 4
            end = middle
        elif array[middle] < target:
            start = middle
        else : #array[middle] = target 
            return middle + 1

result = jr_binary_search(n, target, array)



# 무한루프 해결
import math
def jr_binary_search2(n, target, array):
    start = 0
    end = n-1 #인덱스 번호
    middle = math.floor((start+end)/2)

    while array[middle] != target: 
        middle = math.floor((start+end)/2)
        if (start > end): #무한루프 해결 !!!!!
            break
        if array[middle] > target:
            end = middle - 1 #end값 조정 -> 무한루프 해결
        elif array[middle] < target:
            start = middle + 1 #start값 조정 -> 무한루프 해결
        else : #array[middle] = target 
            return middle + 1

n, target = 10, 7
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
result = jr_binary_search2(n, target, array)

if result == None:
    print('결과없음')
else:
    print(result)

#책 풀이
#10 7
#1 3 5 7 9 11 13 15 17 19
#return 4
# 재귀함수로 구현한 이진 탐색
def binary_search_by_recursive(array, target, start = 0, end = n-1):
    if start > end :
        return None
    mid = (start+end) // 2

    if array[mid] == target : 
        return mid
    elif array[mid] > target :
        return binary_search_by_recursive(array, target, start, mid-1)
    else:
        return binary_search_by_recursive(array, target, mid+1, end)

n, target = 10, 7 #map(int, input().split())
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] #list(map(int, input().split()))

result = binary_search_by_recursive(array, target)

if result == None:
    print('결과없음')
else:
    print(result+1)


# 반복문으로 구현한 이진 탐색
def binary_search_by_loop(rray, target, start = 0, end = n-1):
    while start <= end :
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else :
            start = mid + 1
    return None

n, target = 10, 6 #map(int, input().split())
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] #list(map(int, input().split()))

result = binary_search_by_loop(array, target)

if result == None:
    print('결과없음')
else:
    print(result+1)
####################################################################################
#3. 트리 자료구조
#노드와 노드의 연결로 표현, 노드는 정보의 단위로서 어떠한 정보를 가지고 있는 개체
#트리 구조의 특징
#1. 트리는 부모 노드와 자식 노드의 관계로 표현됨
#2. 트리의 최상단 노드를 루트 로드라고 함
#3. 트리의 최하단 노드를 말단 노드라고 함
#4. 트리에서 일부를 뗴어내도 트리구조이며, 이를 서브 트리라고 함
#5. 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합


#3-1. 이진 탐색 트리
#이진 탐색 트리의 특징
#1. 부모 노드보다 왼쪽 자식 노드가 작음
#2. 부모 노드보다 오른쪽 자식 노드가 큼

#3-2. 빠르게 입력받기
import sys
input_data = sys.stdin.readline().rstrip()
print(input_data)