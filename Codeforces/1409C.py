for _ in range(int(input())):
    n,x,y=map(int, input().split())
    res=[1000000001]*n
    for start in range(1,51):
        for diff in range(1,51):
            a=[]
            for ele in range(start,start+n*diff,diff):
                a.append(ele)
            if (x in a) and (y in a) and (res[n-1]>a[n-1]):
                res=a
    print(*res)