n=int(input())
x=0
for i in range(n):
    a=list(input())
    if a[1]=="+":
        x+=1
    else:
        x-=1
print(x)