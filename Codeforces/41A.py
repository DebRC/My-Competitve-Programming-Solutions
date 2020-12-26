s=list(input())
t=list(input())
if len(s)!=len(t):
    print("NO")
else:
    n=len(s)
    flag=0
    for i in range(n):
        if s[i]!=t[n-i-1]:
            flag=1
            break
    if flag==1:
        print("NO")
    else:
        print("YES")