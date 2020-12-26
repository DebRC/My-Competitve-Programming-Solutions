n=int(input())
a=[0]*n
for i in range(n):
    a[i]=input()
#print(a)
temp=sorted(a)
temp2=sorted(a,reverse=True)
#print(temp)
#print(temp2)
if a==temp:
    print("INCREASING")
elif a==temp2:
    print("DECREASING")
else:
    print("NEITHER")