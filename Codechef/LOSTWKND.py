# cook your dish here
t=int(input())
while(t>0):
    t-=1
    a=list(map(int, input().split()))
    p=a[5]
    a=a[:5]
    for i in range(5):
        a[i]=p*a[i]
    add=sum(a)
    if add<=120:
        print('No')
    elif add>120:
        print('Yes')