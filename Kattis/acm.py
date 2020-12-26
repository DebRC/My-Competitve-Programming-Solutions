a=[]
while(1):
    temp=list(input().split())
    temp[0]=int(temp[0])
    if temp[0]==-1:
        break
    a.append(temp)
#print(a)
n=len(a)
#print(n)
new=[]
for i in range(n):
    temp=[a[i][0],a[i][1]]
    if (a[i][2]=="right") and (temp not in new):
        new.append(temp)
#print(new)
total=0
for i in range(len(new)):
    for j in range(n):
        if a[j][2]=='right' and a[j][1]==new[i][1]:
            break
        if a[j][2]=='wrong' and a[j][1]==new[i][1]:
            new[i][0]+=20
    #print(new)
    total+=new[i][0]
print(len(new),total)