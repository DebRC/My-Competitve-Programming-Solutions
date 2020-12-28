# cook your dish here
t=int(input())
while(t>0):
    t-=1
    q,i=map(float, input().split())
    if(q>1000):
        print("%.6f"%((q*i)-(0.1*q*i)))
    else:
        print("%.6f"%(q*i))