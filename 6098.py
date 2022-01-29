#2차원 배열 d만들기
d=[]
for i in range(11):
  d.append([])
  for j in range(11):
    d[i].append(0)

#2차원배열에 미로 한줄씩 입력
for i in range(10):
  a=input().split()
  for j in range(10):
    d[i+1][j+1]=int(a[j])

#미로 탐색 알고리즘
i=2
j=2
while True:
    if d[i][j]==2:
      d[i][j]=9
      break
    elif d[i][j+1]!=1:
      d[i][j]=9
      j+=1
    elif d[i+1][j]!=1:
      d[i][j]=9
      i+=1
    else:
      d[i][j]=9
      break

for i in range(1,11):
  for j in range(1,11):
    print(d[i][j],end=' ')
  print()
