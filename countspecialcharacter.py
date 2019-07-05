b=input()
count=0
for i in range(len(b)):
  if(b[i].isdigit() or b[i].isalpha() or b[i]==(" ")):
    continue
  else:
    count+=1
print(count)