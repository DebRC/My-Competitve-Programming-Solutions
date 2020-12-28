# cook your dish here
for _ in range(int(input())):
    k=int(input())
    a=[[],[],[],[],[],[],[],[]]
    for i in range(8):
        for j in range(8):
            a[i].append(0)
    a[0][0]='O'
    k-=1
    for i in range(8):
        for j in range(8):
            if(j==0 and i==0):
                continue
            if(k!=0):
                a[i][j]='.'
                k-=1
            else:
                a[i][j]='X'
    for i in range(8):
        for j in range(8):
            print(a[i][j],end="")
        print()