k=int(input())
pk=[]
for i in range(0,k):
 ij=input()
 pk.append(ij)
ff=[]
for i in zip(*pk):
 if(i.count(i[0])==len(i)):
  ff.append(i[0])
 else:
  break
print(''.join(ff))
