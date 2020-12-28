# cook your dish here
t=int(input())
while(t>0):
    n,k=map(int, input().split(' '))
    a=list(map(int, input().split()))
    new=[]
    for i in range(n-k+1):
        add=0
        for j in range(i,i+k):
            add+=a[j]
            new.append(add)
    print(max(new))
    t-=1