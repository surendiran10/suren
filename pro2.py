s,q=input().strip().split()
q=int(q)
h=0
while h<len(s)-1 and q:
 if(s[h]>s[h+1]):
  q-=1
  s=s[:h]+s[h+1:]
  if(h!=0):
   h-=1
 else:
  h+=1
lk=s[:len(s)-q]
print(lk)
