# cook your dish here
for _ in range(int(input())):
    n,b=map(int, input().split())
    temp=0
    max_area=0
    for i in range(n):
        w,h,p=map(int, input().split())
        if(p<=b):
            temp=w*h
            if(temp>max_area):
                max_area=temp
    if(max_area==0):
        print("no tablet")
    else:
        print(max_area)