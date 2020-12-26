mod=10**9+7
x,y=map(int, input().split())
a=[x,y,y-x,-x,-y,x-y]
n=int(input())
if n%6==0:
    print(a[5]%mod)
else:
    print(a[(n%6)-1]%mod)