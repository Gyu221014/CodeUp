a,m,d,n = input().split()
a=int(a)
m=int(m)
d=int(d)
n=int(n)

if(n-a==0):
    print(a)
else:
    for i in range(1,n):
        j=a*m+d
        a=j
    print(j)