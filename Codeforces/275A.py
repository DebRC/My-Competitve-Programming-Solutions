a=[]
for i in range(3):
    temp=list(map(int, input().split()))
    a.append(temp)
b=[[1,1,1],[1,1,1],[1,1,1]]
for i in range(3):
    for j in range(3):
        if a[i][j]&1:
            #middle
            if b[i][j]==1:
                b[i][j]=0
            else:
                b[i][j]=1
            #down
            if i+1<=2:
                if b[i+1][j]:
                    b[i+1][j]=0
                else:
                    b[i+1][j]=1
            #top
            if i-1>=0:
                if b[i-1][j]:
                    b[i-1][j]=0
                else:
                    b[i-1][j]=1
            #right
            if j+1<=2:
                if b[i][j+1]:
                    b[i][j+1]=0
                else:
                    b[i][j+1]=1
            #left
            if j-1>=0:
                if b[i][j-1]:
                    b[i][j-1]=0
                else:
                    b[i][j-1]=1
            '''#corner down right
            if i+1<=2 and j+1<=2:
                if b[i+1][j+1]:
                    b[i+1][j+1]=0
                else:
                    b[i+1][j+1]=1
            #corner down left
            if i+1<=2 and j-1>=0:
                if b[i+1][j-1]:
                    b[i+1][j-1]=0
                else:
                    b[i+1][j-1]=1
            #corner up right
            if i-1>=0 and j+1<=2:
                if b[i-1][j+1]:
                    b[i-1][j+1]=0
                else:
                    b[i-1][j+1]=1
            #corner up left
            if i-1<=2 and j-1>=0:
                if b[i-1][j-1]:
                    b[i-1][j-1]=0
                else:
                    b[i-1][j-1]=1'''
for i in range(3):
    for j in range(3):
        print(b[i][j],end="")
    print()