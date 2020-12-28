# cook your dish here
for _ in range(int(input())):
    n=int(input())
    i=1
    count=0
    while(n>0):
        n-=i
        i+=1
        if(n<0):
            break
        else:
            count+=1
    print(count)