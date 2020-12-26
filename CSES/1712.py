mod=10**9+7
for _ in range(int(input())):
    a,b,c=map(int, input().split())
    print(pow(a,pow(b,c,mod-1),mod))