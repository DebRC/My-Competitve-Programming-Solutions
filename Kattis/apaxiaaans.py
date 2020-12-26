a=list(input())
new=[a[0]]
n=len(a)
flag=0
for i in range(1,n):
    if a[i]!=a[i-1]:
        flag=1
    elif a[i]==a[i-1]:
        flag=0
    if flag==1:
        new.append(a[i])
print("".join(new))