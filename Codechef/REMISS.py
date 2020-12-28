# cook your dish here
t=int(input())
while(t>0):
    t-=1
    a,b=map(int, input().split(' '))
    if(a>b):
        print(a,a+b)
    elif(b>a):
        print(b, a+b)
    else:
        print(a, a+b)