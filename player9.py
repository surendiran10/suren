ns,ms=map(int,input().split())
zs=0
for i in range (ns,ms+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else: 
        zs+=1
print(zs)
