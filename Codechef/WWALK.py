# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    suma=0
    sumb=0
    total=0
    for i in range(n):
        if (suma==sumb and a[i]==b[i]):
            total+=b[i]
        suma+=a[i]
        sumb+=b[i]
    print(total)