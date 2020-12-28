# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n):
        k=int(input())
        if k in a:
            a.remove(k)
        else:
            a.append(k)
    print(a[0])