N = int(input())
scores = list(map(int, input().split()))
M = max(scores)
summ = 0

for score in scores:
    summ += score/M*100
  
print(summ/N)



# 한 과목의 점수를 구하는 식을 총합과 관련된 식으로 바꿀 수 있음
#a/100 + b/100 + c/100 == (a+b+c)/100

summ = 0
summ = sum(scores)/M * 100

print(summ/N)
