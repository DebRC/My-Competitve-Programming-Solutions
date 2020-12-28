for _ in range(int(input())):
    s=input()
    s=list(s)
    n=len(s)
    flag=0
    if(s[0]==s[1]):
        flag=1
    for i in range(0,n-2,2):
        if(s[i]!=s[i+2]):
            flag=1
    for i in range(1,n-2,2):
        if(s[i]!=s[i+2]):
            flag=1
    if(flag==1):
        print("NO")
    else:
        print("YES")