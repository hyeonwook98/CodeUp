a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
minp=0
minj=0
if (a<=b and a<=c):
  minp=a
elif (b<=a and b<=c):
  minp=b
elif (c<=a and c<=b):
  minp=c

if d<e:
  minj=d
else:
  minj=e
sum=minp+minj
sum+=(sum)*0.1
print(sum)
