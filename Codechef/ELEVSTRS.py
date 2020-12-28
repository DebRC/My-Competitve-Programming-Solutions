# cook your dish here
for _ in range(int(input())):
    n,v1,v2=map(int, input().split())
    t1=(n*(2**0.5))/v1
    t2=(2*n)/v2
    #print(t1,t2)
    if(t1>t2):
        print("Elevator")
    else:
        print("Stairs")