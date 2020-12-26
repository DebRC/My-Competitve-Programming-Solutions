a,b,n=map(int, input().split())
flag=-1
for i in range(10):
    if (a*10+i)%b==0:
        flag=a*10+i
        flag=str(flag)+str(0)*(n-1)
        break
print(flag)