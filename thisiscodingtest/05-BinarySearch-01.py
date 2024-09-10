#부품 찾기

#가게가 가진 부품
N = 5
store = [8, 3, 7, 9, 2]

#손님이 요청한 부품
M = 3
customer = [5, 7, 9]

#손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes, 없으면 no
#출력 : no yes yes


#2. 이진 탐색(Binary Search) : 반으로 쪼개면서 탐색하기
#위치 변수 3개 이용 - 범위의 시작점, 끝점, 중간점 -> 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교

def binary_search(array, target, start, end):
    array.sort() #이진탐색을 위한 array 정렬
    while start <= end : 
        mid = (start+end)//2
        if array[mid] == target :
            return mid
        elif array[mid] > target :
            end = mid - 1
        else:
            start = mid + 1
    return None

#입력
#N = int(input())
#store = list(map(int, input().split()))
#M = int(input())
#customer = list(map(int, input().split()))

for target in customer:
    result = binary_search(store, target, 0, N-1)
    if result == None:
        print('no', end= ' ')
    else :
        print('yes', end = ' ')


#############################################################
#책 풀이1 - 계수 정렬
N = 5 #int(input())
N_count = [0] * 1000001 #1<= N <= 1000000
store = [8, 3, 7, 9, 2]

for i in store:
    N_count[i] = 1 #존지하는 지만 확인하면 되므로 +1안해도 됨

#for i in input().split():
#    N_count[int(i)] = 1

M = 3 #int(input())
customer = [5, 7, 9] #list(map(int, input().split()))

for i in customer:
    if N_count[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end =' ')
#############################################################
#책 풀이2 - 집합 자료형 이용

N = 5
store = [8, 3, 7, 9, 2]
M = 3
customer = [5, 7, 9]

array = set(store) # 집합 자료형 -> set(map(int, input().split()))
for target in customer:
    if target in array :
        print('yes', end = ' ')
    else:
        print('no', end = ' ')