# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    temp=[]
    for i in range(n):
        if a[i] not in temp:
            temp.append(a[i])
    print(len(temp))