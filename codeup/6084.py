h,b,c,s=input().split()
h=int(h)
b=int(b)
c=int(c)
s=int(s)

PCM = h*b*c*(s/8/1024/1024)

print(format(PCM,".1f"), "MB")