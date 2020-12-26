while(1):
    n=int(input())
    if n==-1:
        break
    prev=0
    count=0
    for i in range(n):
        s,t=map(int, input().split())
        t1=t-prev
        prev=t
        count+=(s*t1)
    print(count,"miles")