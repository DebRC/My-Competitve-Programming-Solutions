# cook your dish here
p1,p2=0,0
t1,t2=0,0
l1,l2=0,0
for _ in range(int(input())):
    p1,p2=map(int, input().split())
    t1+=p1
    t2+=p2
    if(t1>t2 and t1-t2>l1):
        l1=t1-t2
    elif(t2>t1 and t2-t1>l2):
        l2=t2-t1
if(l1>l2):
    print(1,l1)
else:
    print(2,l2)