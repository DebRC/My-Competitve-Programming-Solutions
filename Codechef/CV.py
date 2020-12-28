# cook your dish here
def check(x):
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
        return 1
    else:
        return 0
for _ in range(int(input())):
    n=int(input())
    a=input()
    c=0
    for i in range(n-1):
        if(check(a[i])==0 and check(a[i+1])==1):
            c+=1
    print(c)