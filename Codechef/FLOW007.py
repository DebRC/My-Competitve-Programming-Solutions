# cook your dish here
t=int(input())
while(t>0):
    t-=1
    num=list(input())
    num.reverse()
    for i in range(len(num)):
        if(num[i]!='0'):
            num=num[i:]
            print("".join(num))
            break