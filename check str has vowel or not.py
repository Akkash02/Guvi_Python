str = input()
count = 0
for i in str:
	if( i=='A' or i=='a' or i=='E' or i=='e'
	or i=='I' or i=='i' or i=='O' or i=='o'
	or i=='U' or i=='u'):
		count +=1;
if(count!=0):    
  print ("yes")
else:
  print("no")  