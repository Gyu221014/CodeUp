a = input()
n = int(a,16)
m = int('F',16)

for i in range(1,m+1):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')