# cook your dish here
for _ in range(int(input())):
    n=int(input())
    new=[]
    a,b=0,0
    for i in range(n):
        g=list(map(int, input().split()))
        new.append(g)
    for i in range(n):
        share_a=(new[i][2]/(new[i][2]+new[i][1]))*new[i][0]
        a+=share_a
        share_b=(new[i][1]/(new[i][2]+new[i][1]))*new[i][0]
        b+=share_b
    print(a,b)