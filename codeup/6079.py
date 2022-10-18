n = int(input())
a=0
b=1

if(n==0):
    print(n)
while n>=b:
    a+=1    
    b=b+a 
    if n<b:
        print(a)