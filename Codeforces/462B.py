n,k=map(int,input().split())
s=list(input())
d={}
for i in s:
    try:
        d[i]+=1
    except:
        d[i]=1
new=[]
for keys in d:
    new.append(d[keys])
new.sort(reverse=True)
i=0
total=0
while(k>0):
    if new[i]<=k:
        total+=(new[i]**2)
        k-=new[i]
        i+=1
    else:
        total+=k**2
        break
print(total)