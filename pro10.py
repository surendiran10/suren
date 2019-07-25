c=int(input())
ch=[int(o) for o in input().split(" ")]
s=0
for p in range(c):
      for g in range(p):
           if(ch[g]<ch[p]):
                s+=ch[g]
print(s)
