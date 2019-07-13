s=int(input())
bs=list(map(int,input().split()))
cs=[]
for i in bs:
  if (bs.count(i)>1):
    if i not in cs:
      cs.append(i)
if (len(cs)==0):
  print('unique')
print(*cs)
