for _ in range(int(input())):
    s,n=map(int, input().split())
    result=0
    if(n%2==0 and n>=2):
        if(s<n):
            if (s==1):
                result=1
            elif(s%2==0):
                result=1
            else:
                result=2;
        else:
            k=s%n;
            q=s//n
            result=s//n
            if(k>0):
                if(k==1):
                    result=result+1
                elif(k%2!=0 and k>1):
                    result=result+2
                else:
                    result=result+1;
    print(result)