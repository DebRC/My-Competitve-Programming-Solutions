t=int(input())
for i in range(t):
    n,m=[int(x) for x in input().split(' ')]
    s=0
    for i in range(n):
        for j in range(m):
            if(j==0 or i==0):
               s+=1 
            else:
                s+=2
    print(s-1)