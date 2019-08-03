a,b=map(int,input().split())
c=list(map(int,input().split()))[:a]
d=list(map(int,input().split()))[:b]
flag = 0
if((set(d) & set(c))== set(d)): 
    flag = 1
if(flag):
  print("YES") 
else:
  print("NO")   
   
    
