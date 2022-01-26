a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
d=1
while True:
 if (d%a)==0 and (d%b)==0 and (d%c)==0:
   break
 else:
   d+=1

print(d)
