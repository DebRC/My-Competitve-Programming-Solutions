n,m=map(int, input().split())
a=list(map(int, input().split()))
b=[0]*n
s=set()
for i in range(n-1,-1,-1):
    s.add(a[i])
    b[i]=len(s)
for i in range(m):
    print(b[int(input())-1])