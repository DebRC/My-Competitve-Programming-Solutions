# cook your dish here
for _ in range(int(input())):
    n,m,k=map(int, input().split())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    count1=0
    count2=0
    for i in range(1,n+1):
        if i in a and i in b:
            count1+=1
        if i not in a and i not in b:
            count2+=1
    print(count1,count2)