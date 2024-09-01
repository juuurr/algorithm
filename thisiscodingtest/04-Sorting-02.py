#성적이 낮은 순서로 학생 출력하기

N = int(input())
dic = {}
for i in range(N):
    input_data = input().split()
    dic[input_data[0]] = int(input_data[1])
print(dic)
sorted_list = sorted(dic.items(), key=lambda x : x[1])

for i in sorted_list:
    print(i[0], end = ' ')


#책풀이 - 리스트로도 가능!
N = int(input())
array = []
for i in range(N):
    input_data = input().split()
    array.append((input_data[0], input_data[1]))

array = sorted(array, key = lambda x: x[1])

for student in array:
    print(student[0], end = ' ')