# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    count=0
    for i in range(n):
        if(i==0):
            if(a[i]>=b[i]):
                count+=1
        else:
            if(a[i]-a[i-1]>=b[i]):
                count+=1
    print(count)