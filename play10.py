ns=input().split()
xs=list(ns[0])
count=0
ys=list(ns[1])
for i in range(0,len(xs)):
  if(xs[i]!=ys[i]):
    count+=1
if(count==1):
  print("yes")
else:
  print("no")
