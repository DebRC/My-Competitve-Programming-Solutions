for _ in range(int(input())):
    n=int(input())
    d={}
    for i in range(n):
        s=input()
        for i in s:
            try:
                d[i]+=1
            except:
                d[i]=1
    flag=0
    #print(d)
    for keys in d:
        if d[keys]%n!=0:
            flag=1
    if flag:
        print("NO")
    else:
        print("YES")