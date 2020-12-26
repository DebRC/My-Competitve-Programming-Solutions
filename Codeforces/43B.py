s1=input()
s2=input()
d={}
for i in s1:
    if i!=' ':
        try:
            d[i]+=1
        except:
            d[i]=1
flag=0
for i in s2:
    if i!=' ':
        try:
            if d[i]==0:
                flag=1
                break
            d[i]-=1
        except:
            flag=1
            break
if flag:
    print("NO")
else:
    print("YES")