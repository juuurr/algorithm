h, b, c, s = input().split()
h, b, c, s = int(h), int(b), int(c), int(s)
to = h*b*c*s
fin = to/8/1024/1024
print(format(fin, '.1f') + ' MB')
