# cook your dish here
t=int(input())
while(t>0):
    people,balance=map(int, input().split(' '))
    a=list(map(int, input().split()))
    new=[]
    for i in range(people):
        if(a[i]<=balance):
            new.append("1")
            balance-=a[i]
        else:
            new.append("0")
    print("".join(new))
    t-=1