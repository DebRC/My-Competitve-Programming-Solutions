n,w,h=map(int, input().split())
length=((w*w)+(h*h))**0.5
for i in range(n):
    temp=float(input())
    if temp<=length:
        print("DA")
    else:
        print("NE")