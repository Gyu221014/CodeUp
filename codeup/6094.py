n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

for i in range(n-1) :
    if(a[0]<a[1]):
        del a[1]
    else:
        del a[0]

print(a[0])