# cook your dish here
for _ in range(int(input())):
    n,k=map(int, input().split())
    ns=list(input().split())
    ks=[]
    for i in range(k):
        temp=list(input().split())
        t=int(temp[0])
        for j in range(1,t+1):
            ks.append(temp[j])
    for i in range(n):
        if ns[i] in ks:
            print("YES", end=" ")
        else:
            print("NO", end=" ")
    print()