# cook your dish here
t=int(input())
while(t>0):
    t-=1
    a,b=map(int, input().split(' '))
    if(a>b):
        print('>')
    elif(a<b):
        print('<')
    else:
        print('=')