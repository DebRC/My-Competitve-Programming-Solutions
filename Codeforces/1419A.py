for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input()))
    if n&1:
        even=0
        odd=0
        for i in range(0,n,2):
            if a[i]&1:
                odd+=1
            else:
                even+=1
        if odd!=0:
            print(1)
        else:
            print(2)
    else:
        even=0
        odd=0
        for i in range(1,n,2):
            if a[i]&1:
                odd+=1
            else:
                even+=1
        if even!=0:
            print(2)
        else:
            print(1)