for _ in range(int(input())):
    n,x=map(int, input().split())
    a=list(map(int, input().split()))
    a.sort()
    #print(a)
    if(a[n-1]<=x):
        print(n)
        continue
    for i in range(n):
        if(x<=a[i]):
            start=i
            #print(start, end=" ")
            break
    count=0
    for i in range(start,n):
        if x<=a[i]:
            while(x<a[i]):
                x=x*2
                count+=1
        count+=1
        x=a[i]*2
        #print(count, end=" ")
    #print(count, end=" ")
    day=start+count
    if(start):
        count=0
        start-=1
        for i in range(start,n):
            if(x<=a[i]):
                while(x<a[i]):
                    x=x*2
                    count+=1
            count+=1
            x=a[i]*2
        if(count+start>day):
            print(day)
        else:
            print(start+count)
    else:
        print(day)