# cook your dish here
t=int(input())
while(t>0):
    t-=1
    n=list(map(int, input()))
    a=[]
    for i in range(len(n)-1,-1,-1):
        a.append(n[i])
    if (a==n):
        print("wins")
    else:
        print("losses")