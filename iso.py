a,d=map(str,input().split())
if(len(a)!=len(d)):
    print("no")
else :
    s12=[a.count(i) for i in a]
    s22=[d.count(i) for i in d]
if(s12==s22):
    print("yes")
else:
    print("no")
