# cook your dish here
t=int(input())
while(t>0):
    s=list(input())
    sa,sb=map(int,input().split(' '))
    pos_a=s.index('A')
    pos_b=s.index('B')
    flag=0
    while(pos_a<pos_b):
        pos_a=pos_a+sa
        pos_b=pos_b-sb
        if(pos_a==pos_b):
            flag=1
            break
    if(flag==1):
        print("unsafe")
    else:
        print("safe")
    t-=1