#2차원배열 0만들기
a=[]
h,w=input().split()
h=int(h)+1
w=int(w)+1
for i in range(h):
  a.append([])
  for j in range(w):
    a[i].append(0)


n=int(input())
for i in range(n):
  l,d,x,y=input().split()
  l=int(l)
  d=int(d)
  x=int(x)
  y=int(y)

  if d==0:
    for j in range(y,y+l):
      a[x][j]=1
  else:
    for j in range(x,x+l):
      a[j][y]=1

for i in range(1,h):
  for j in range(1,w):
    print(a[i][j],end=' ')
  print()

