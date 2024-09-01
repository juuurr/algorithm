#위에서 아래로
#N개의 숫자를 큰 순서대로 정렬


N = int(input())
array = []

for i in range(N):
    array.append(int(input()))

array.sort(reverse = True)
for num in array:
    print(num, end = ' ')