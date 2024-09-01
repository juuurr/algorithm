# 두 배열의 원소 교체
# K번의 바꿔치기 연산을 통해 만들 수 있는 A 배열의 모든 원소의 합의 최댓값 구하기
#input
#N, K = map(int, input().split())
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))


N, K = 5, 3 #최대 K번의 바꿔치기, N은 배열의 길이
a = [1,2,5,4,3]
b = [5,5,6,6,5]

a = sorted(a, reverse = True) #내림차순
b = sorted(b) #오름차순


for _ in range(K):
    a.pop()
for _ in range(K):
    a.append(b.pop())
print(sum(a))

#히든케이스 고려하지 못함 -> b의 원소가 a보다 작은 경우 변경하면 x

####################################################################################
#히든케이스 고려한 풀이
a = [1,4,4,4,5]
b = [1,1,2,3,2]

a = sorted(a, reverse = True) #내림차순
b = sorted(b, reverse = True)
a_min = []
for _ in range(K):
    a_min.append(a.pop())

for i in range(K):
    if b[i] >= a_min[i]:
        a.append(b[i])
    else:
        a.append(a_min[i])

print(sum(a))


####################################################################################
#책풀이

a = [1,2,5,4,3]
b = [5,5,6,6,5]

a.sort() #오름차순
b.sort(reverse = True)

for i in range(K):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))