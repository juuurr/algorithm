a,m,d,n = input().split()
a,m,d,n = int(a), int(m), int(d), int(n)

summ = 0
i = 0

while i < n-1:
  summ += m**i
  i += 1

print(a*m**(n-1) + summ*d)

#첫번째 수도 수열에 포함해야 함 !
