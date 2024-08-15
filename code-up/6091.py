
lis = input().split()
lis = list(map(int, lis))

liss = sorted(lis)

a = liss[0]
b = liss[1]
c = liss[2]

lis2 = []
for i in [b,c]:
    if i%a == 0:
        lis2.append(i//a)
    else:
        lis2.append(i)

liss2 = sorted(lis2)
aa = liss2[0]
bb = liss2[1]

lis3 = []
if bb%aa == 0:
    lis3.append(bb//aa)
else:
    lis3.append(bb)

print(a*aa*lis3[0])
