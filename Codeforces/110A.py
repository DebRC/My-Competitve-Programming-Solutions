n=list(map(int, input()))
total=0
for i in n:
    if i==7 or i==4:
        total+=1
total=[int(x) for x in str(total)]
total2=0
for i in total:
    if i==7 or i==4:
        total2+=1
if total2==len(total):
    print("YES")
else:
    print("NO")