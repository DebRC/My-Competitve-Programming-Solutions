s=input()
n=int(input())
a=[]
for i in range(n):
    temp=input()
    a.append(temp)
print(s)
print()
for i in range(n):
    for j in range(len(a[i])):
        print(a[i][j],end="")
    print()