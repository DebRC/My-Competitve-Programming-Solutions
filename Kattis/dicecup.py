n,m=map(int, input().split())
if n==m:
    print(n+1)
elif n<m:
    for i in range(n+1,m+2):
        print(i)
else:
    for i in range(m+1,n+2):
        print(i)