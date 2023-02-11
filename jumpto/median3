# 세 정수의 중앙값 구하기

#방법 1
k = list(map(int, input().split()))
sork = sorted(k)
print(sork[1])

#방법 2
a,b,c = map(int, input().split())
med = 0
if a >= b:
  if b >= c: med = b
  elif c >= a: med = a
  else: med = c
elif a > c: med = a
elif b > c: med = c
else: med = b

print(med)

#방법 3
def med3(a,b,c):
  if a >= b:
    if b >= c: return b 
    elif c >= a: return a
    else: return c
  elif a > c: return a
  elif b > c: return c
  else: return b

a,b,c = map(int, input().split())
med3(a,b,c)
