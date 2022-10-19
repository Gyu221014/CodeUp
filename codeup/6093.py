n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

d = []
for i in range(n) :
  d.append(a[-1-i])

for i in range(0, n) :
  print(d[i], end=' ')