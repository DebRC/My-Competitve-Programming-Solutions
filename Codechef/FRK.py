# cook your dish here
n=int(input())
c=0
for i in range(n):
    a=list(input())
    for j in range(len(a)-1):
        #print(a[j], end="")
        if (a[j]=="c" and a[j+1]=="h") or (a[j]=="h" and a[j+1]=="e") or (a[j]=="e" and a[j+1]=="f"):
            c+=1
            break
print(c)