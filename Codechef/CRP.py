n=int(input())
while(n>0):
    a,b=input().split()
    a_m=int(a)
    b_n=int(b)
    if(a_m<300 or b_n<280):
        print("-1")
    else:
        res=(a_m*b_n-84000)%(10**9+7)
        print(res)
    n-=1