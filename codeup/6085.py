w,h,b=input().split()
w=int(w)
h=int(h)
b=int(b)

whb = w*h*(b/8/1024/1024)

print(format(whb,".2f"), "MB")