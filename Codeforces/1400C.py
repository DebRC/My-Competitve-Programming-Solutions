for _ in range(int(input())):
    s=list(map(int, input()))
    #print(s)
    x=int(input())
    n=len(s)
    w=[1]*(n)
    #print(w)
    for i in range(n):
        if s[i]==0:
            if i>=x:
                w[i-x]=s[i]
            if i+x<n:
                w[i+x]=s[i]
        #print(w)
        is_there = 1
    for i in range(n):
        if s[i]==1:
            if (i-x<0 or w[i-x]==0) and (i+x>=n or w[i+x]==0):
                is_there=0
                break
    if is_there==0:
        print(-1)
    else:
        print("".join([str(x) for x in w]))