s=153
sum=0
temp=s
while(temp>0):
	dig=temp%10
	sum+=dig**3
	temp//=10
	
	
if(s==sum):
	print("yes")
else:
	print("no")
