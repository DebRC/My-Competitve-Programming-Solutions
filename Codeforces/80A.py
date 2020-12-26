def isPrime(n):
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            return False
    return True
n,m=map(int,input().split())
prime=0
for i in range(n+1,m+1):
    if isPrime(i):
        prime=i
        break
if prime==m:
    print("YES")
else:
    print("NO")