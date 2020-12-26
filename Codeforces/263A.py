a=[]
for i in range(5):
    temp=list(map(int, input().split()))
    a.append(temp)
    if temp.count(1)!=0:
        x,y=i,temp.index(1)
print(abs(2-x)+abs(2-y))