# cook your dish here
t=int(input())
while(t>0):
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()
    print(a[0]+a[1])
    t-=1