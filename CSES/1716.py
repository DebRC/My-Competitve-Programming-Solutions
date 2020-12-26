mod=(10**9)+7
high=(2*(10**6))+1
fact=[1]*high
def power(a,n,m):
    res=1
    while(n):
        if n%2==1:
            res=((res%m)*(a%m))%m
            n-=1
        else:
            a=((a%m)*(a%m))%m
            n//=2
    return res
def factorial():
    for i in range(2,high):
        fact[i]=(i*fact[i-1])%mod
factorial()
n,m=map(int,input().split())
upper=(m+n-1)%mod
print(((fact[upper])*power((fact[n-1]*fact[m])%mod,mod-2,mod))%mod)