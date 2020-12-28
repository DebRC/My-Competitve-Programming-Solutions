# cook your dish here
for _ in range(int(input())):
    d,n=map(int, input().split())
    for i in range(d):
        n=int(n*(n+1)/2)
    print(n)