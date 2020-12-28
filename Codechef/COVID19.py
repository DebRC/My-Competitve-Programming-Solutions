t=int(input())
while(t>0):
    n=int(input())
    x=list(map(int, input().split()))
    a=[]
    for i in range(len(x)):
        count=1
        for j in range(i,len(x)-1):
            if x[j+1]-x[j]<=2:
                count+=1
            else:
                break
        for j in range(i,0,-1):
            if x[j]-x[j-1]<=2:
                count+=1
            else:
                break
        a.append(count)
    print(min(a),max(a))    
    t-=1