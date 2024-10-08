#연산의 개수 N(100,000)
#x : 연산에 대한 정보를 나타내는 정수
# if x != 0 : 배열에 x 삽입
# ix x == 0 : 배열에서 절댓값이 가장 작은 값 출력 후 값 제거
#(절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력)
#x는 2**(-31) ~ 2**(31)

#참고 : https://littlefoxdiary.tistory.com/3

N = 13
arr = [1, 1, -1, -1, 2, -2, 0, 0, 0, 0, 0, 0, 0]
len(arr)


import heapq
h = []

for i in range(N):
    if arr[i] != 0:
        heapq.heappush(h, (abs(arr[i]), arr[i]))
        print(h)
    else:
        if len(h) > 0:
            print(heapq.heappop(h)[1])
        else: 
            print(0)

##############################################입력 고
#풀이1 - 시간초과
import heapq

N = int(input())
h = []

for i in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(h, (abs(x), x))
    else:
        if len(h) > 0:
            print(heapq.heappop(h)[1])
        else: 
            print(0)


#풀이2 - 시간초과
import heapq
N = int(input())
h = []

for i in range(N): #O(N)
    x = int(input())
    if x != 0:
        heapq.heappush(h, (abs(x), x)) #O(logN)
    elif len(h) > 0: # x == 0
        print(heapq.heappop(h)[1]) #O(logN)
    else : # len(h) < 0 and x == 0
        print(0)

#N*(logN)
#100,000 * 100 * log(10)
#10**7 * log(10) - 1억(1초)


#100,000은 입력 받는거부터 시간초과가 날 수 있음 -> 빠른 입출력!!
#풀이 3 
import heapq
import sys
N = int(sys.stdin.readline())
h = []

for i in range(N): #O(N)
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(h, (abs(x), x)) #O(logN)
    elif len(h) > 0: # x == 0
        print(heapq.heappop(h)[1]) #O(logN)
    else : # len(h) < 0 and x == 0
        print(0)

#################################강의 풀이 1
import heapq as hq
import sys
input = sys.stdin.readline
pq = []

for _ in range(int(input())):
    x = int(input())
    if x :
        hq.heappush(pq, (abs(x), x)) #abs(x) 기준으로 정렬 -> 이후 x 기준 정렬
    else:
        print(hq.heappop(pq)[1] if pq else 0) #pq가 비어있지 않으면 pop, 비어있으면 0 출력


#강의 풀이 2
import heapq as hq
import sys
input = sys.stdin.readline
min_pq = []
max_pq = []