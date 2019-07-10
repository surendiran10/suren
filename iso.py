s,v=map(str,input().split())
if(len(sn)!=len(vg)):
 print("no")
else:
 s22=[sn.count(i) for i in s]
 s32=[vg.count(i) for i in v]
if(s22==s32):
 print("yes")
else:
 print("no")
