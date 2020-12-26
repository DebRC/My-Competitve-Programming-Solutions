for _ in range(int(input())):
    a=list(map(int, input().split()))
    a.pop()
    n=len(a)
    immigrants=0
    for i in range(1,n):
        if a[i]>2*a[i-1]:
            immigrants+=a[i]-2*a[i-1]
    print(immigrants)