# cook your dish here
for _ in range(int(input())):
    b=int(input())
    b-=2
    n=int(b/2)
    c=0
    for i in range(1,n+1):
        c+=i
    print(c)