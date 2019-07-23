N=int(input(""))
A=int(input(""))
D=int(input(""))
s=0
i=0
while i<N:
	s+=A
	A=A+D
	i+=1
print(s)
