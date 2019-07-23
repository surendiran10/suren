n=int(input(""))
l=[]
for i in range(0,n):
	ele=int(input())
	l.append(ele)
l.sort()
print(l[-1])
