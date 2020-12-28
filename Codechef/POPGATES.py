# cook your dish here
for _ in range(int(input())):
    n,k=map(int, input().split())
    a=list(input().split())
    for i in range(k):
        if a[n-1]=="H":
            for j in range(n):
                if a[j]=="H":
                    a[j]="T"
                else:
                    a[j]="H"
        n-=1
        a=a[:n]
        #print(a)
    print(a.count("H"))