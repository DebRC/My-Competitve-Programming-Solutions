# cook your dish here
for _ in range(int(input())):
    n=int(input())
    x=[]
    y=[]
    for i in range(4*n-1):
        temp1,temp2=map(int, input().split())
        x.append(temp1)
        y.append(temp2)
    x.sort()
    y.sort()
    for i in range(0,4*n-1,2):
        if(i==4*n-2):
            temp1=x[i]
            break
        if(x[i]!=x[i+1]):
            temp1=x[i]
            break
    for i in range(0,4*n-1,2):
        if(i==4*n-2):
            temp2=y[i]
            break
        if(y[i]!=y[i+1]):
            temp2=y[i]
            break
    print(temp1,temp2)