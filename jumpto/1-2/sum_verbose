#1
a, b = map(int, input().split())
if a>b:
  a, b = b, a

sum = 0
i_list = []
for i in range(a, b+1):
  sum += i
  i_list.append(i)

for i in range(len(i_list)-1):
  print(i_list[i], end = ' + ')
print(f'{i_list[len(i_list)-1]} = {sum}')



#2
a, b = map(int, input().split())
if a>b:
  a, b = b, a

sum = 0
for i in range(a, b+1):
  if i < b:
    print(f'{i} + ', end = '')
  else:
    print(f'{b} = ', end = '')
  sum += i
print(sum)


#3
a, b = map(int, input().split())
if a>b:
  a, b = b, a

sum = 0
for i in range(a,b):
  print(f'{i} + ', end = '')
  sum += i

print(f'{b} = ', end = '')
sum += b

print(sum)
