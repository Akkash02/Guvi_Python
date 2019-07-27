a=int(input())
b,c=map(int,input().split())
if a in range(b+1,c):
  print("yes")
else:
  print("no")
