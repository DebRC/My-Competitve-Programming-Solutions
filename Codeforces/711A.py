n=int(input())
s=[]
for i in range(n):
    temp=list(input())
    s.append(temp)
flag=True
for i in range(n):
    if s[i][0]=='O' and s[i][1]=='O':
        flag=False
        s[i][0]='+'
        s[i][1]='+'
        break
    if s[i][3]=='O' and s[i][4]=='O':
        flag=False
        s[i][3]='+'
        s[i][4]='+'
        break
if flag:
    print("NO")
    exit(0)
print("YES")
for i in range(n):
    print(''.join(s[i]))