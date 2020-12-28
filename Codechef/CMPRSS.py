# cook your dish here
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    x.append(0)
    i=0
    while (i<(len(x)-1)):
        k=0
        j=i
        while (x[i+1]==(x[i]+1)):
            k+=1
            i+=1
        if (k>=2):
            if (x[i]==x[len(x)-2]):
                print(str(x[j]) + "..." +str(x[i]),end="")
            else:
                
                print(str(x[j]) + "..." +str(x[i]),end=",")
        else:
            i=j
            if (x[i]==x[len(x)-2]):
                print(str(x[i]),end="")
            else:
                
                print(str(x[i]),end=",")
        i+=1
        
            
    print()    