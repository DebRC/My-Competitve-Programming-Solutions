# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=list(input())
    x,y=0,0
    flag=0
    for i in range(n):
        if(s[i]=="L" and flag!=1):
            x-=1
            flag=1
        elif(s[i]=="R" and flag!=1):
            x+=1
            flag=1
        elif(s[i]=="U" and flag!=2):
            y+=1
            flag=2
        elif(s[i]=="D" and flag!=2):
            y-=1
            flag=2
    print(x,y)