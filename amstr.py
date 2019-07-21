s,k=map(int,input().split())
for j in range(s,k):
    temp=j
    sum=0
    while temp>0:
        digit = temp%10
        sum+=digit**3
        temp//=10
    if (j == sum):
        print(j)
