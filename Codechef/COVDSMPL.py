# cook your dish here
import sys
for _ in range(int(input())):
    n,p=map(int, input().split())
    a=[[0 for i in range(n)] for j in range(n)] 
    for i in range(n):
        for j in range(n):
            print(1,i+1,j+1,i+1,j+1, flush=True)
            x=int(input())
            if(x==-1):
                sys.exit()
            a[i][j]=x
            #print(a)
    print(2)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ",flush=True)
        print(flush=True)
    x=int(input())
    if(x==-1):
        sys.exit()