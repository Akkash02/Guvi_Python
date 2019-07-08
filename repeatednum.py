a=int(input())
li1=list(map(int,input().split()))[:a]
n=len(li1)
li2=[]
for i in range(n):
  k=i+1
  for j in range(k,n):
    if li1[i]==li1[j] and li1[i] not in li2:
      li2.append(li1[i])
li2.sort()
if len(li2)==0:
  print('unique')
else:
  print(*li2)