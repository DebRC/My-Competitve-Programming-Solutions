# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    red,green,blue=0,0,0
    for i in s:
        if i=="R":
            red+=1
        elif i=="B":
            blue+=1
        elif i=="G":
            green+=1
    m=max(red,green,blue)
    print(n-m)