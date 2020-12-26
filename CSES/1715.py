from collections import Counter
mod=(10**9)+7
high=(10**6)+1
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
s=list(input())
n=len(s)
a=Counter(s)
#print(a)
mul=1
for keys in a:
    if a[keys]>1:
        mul=(mul*fact[a[keys]])%mod
print(((fact[n])*power(mul,mod-2,mod))%mod)