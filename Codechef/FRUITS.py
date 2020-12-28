# cook your dish here
for _ in range(int(input())):
    n,m,k=map(int, input().split())
    if(n>m):
        d=n-m-k
    else:
        d=m-n-k
    if(d<0):
        d=0
    print(d)