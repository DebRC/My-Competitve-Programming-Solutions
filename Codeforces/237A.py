n=int(input())
d={}
for i in range(n):
    h,m=map(int, input().split())
    time=h*60+m
    try:
        d[time]+=1
    except:
        d[time]=1
print(max(d.values()))