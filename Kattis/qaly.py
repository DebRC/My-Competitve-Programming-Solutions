n=int(input())
res=0
for i in range(n):
    q,y=map(float,input().split())
    res+=(q*y)
print('%.3f'%res)