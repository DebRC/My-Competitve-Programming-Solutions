# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=list(map(int, input().split()))
    total=0
    for i in range(1,n):
        diff=s[i]-s[i-1]
        total+=(abs(diff)-1)
    print(total)