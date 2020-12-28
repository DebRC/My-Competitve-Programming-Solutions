# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int, input().split()))
    r=list(map(int, input().split()))
    watch=[0,0,0]
    for i in range(n):
        temp=l[i]*r[i]
        if(temp>watch[2]):
            watch[0]=i+1
            watch[1]=r[i]
            watch[2]=temp
        elif(temp==watch[2]):
            if(r[i]>=watch[1]):
                if(r[i]>watch[1]):
                    watch[0]=i+1
                    watch[1]=r[i]
                    watch[2]=temp
                elif(r[i]==watch[1]):
                    if(i+1<watch[0]):
                        watch[0]=i+1
                        watch[1]=r[i]
                        watch[2]=temp
    print(watch[0])