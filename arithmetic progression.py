a,b,c=map(int,input().split())
if 1<=a<=100000:
  print(int((a/2)*(2 * b + (a-1) * c)))