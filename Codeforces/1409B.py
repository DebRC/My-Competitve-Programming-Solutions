for _ in range(int(input())):
    a,b,x,y,n=map(int, input().split())
    #first condition minimising a
    min_a=a-n
    min_b=b
    if min_a<x:
        min_b-=(x-min_a)
        min_a=x
    if min_b<y:
        min_b=y
    res1=min_a*min_b
    #second condition minimising b
    min_a=a
    min_b=b-n
    if min_b<y:
        min_a-=(y-min_b)
        min_b=y
    if min_a<x:
        min_a=x
    res2=min_a*min_b
    print(min(res1,res2))