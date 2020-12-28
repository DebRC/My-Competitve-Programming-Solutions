# cook your dish here
for _ in range(int(input())):
    n,k=map(int, input().split())
    a=list(map(int, input().split()))
    count=0
    for i in range(n):
        a[i]=a[i]+k
        if(a[i]%7==0):
            count+=1
    print(count)