# cook your dish here
t=int(input())
while(t>0):
    t-=1
    n=int(input())
    a=list(map(int, input().split()))
    bal=[0,0,0]
    flag=True
    if a[0]==5:
        for i in range(n):
            if a[i]==5:
                bal[0]+=1
            elif a[i]==10:
                bal[0]-=1
                bal[1]+=1
            elif a[i]==15:
                if bal[1]>=1:
                    bal[1]-=1
                    bal[2]+=1
                else:
                    bal[0]-=2
                    bal[2]+=1
            if (bal[0]<0 or bal[1]<0 or bal[2]<0):
                flag=False
                break
        if flag==True:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")