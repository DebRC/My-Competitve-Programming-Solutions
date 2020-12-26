n=int(input())
a=[0,0,0]
for i in range(n):
    x,y,z=map(int, input().split())
    a[0]+=x
    a[1]+=y
    a[2]+=z
if a[0]==0 and a[1]==0 and a[2]==0:
    print("YES")
else:
    print("NO")