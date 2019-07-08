m=int(input())
n,o=0,1
print(o,end=" ")
for i in range(1,m):
  p=n+o
  print(p,end=" ")
  n,o=o,p
