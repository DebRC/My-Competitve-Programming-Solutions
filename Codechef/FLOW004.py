# cook your dish here
t=int(input())
while(t>0):
    t-=1
    a=list(map(int, input()))
    print(a[0]+a[len(a)-1])