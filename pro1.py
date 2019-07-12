k1=int(input())
pk1=[]
for i in range(0,k1):
 ij=input()
 pk1.append(ij)
ff1=[]
for i in zip(*pk1):
 if(i.count(i[0])==len(i)):
  ff1.append(i[0])
 else:
  break
print(''.join(ff1))
