z=0
a,b=map(int,input().split())
c=list(map(int,input().split()))[:a]
for s in c:
  if s==b:
    z+=1
if(z!=0):
  print("yes")
else:
  print("no")