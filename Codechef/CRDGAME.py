# cook your dish here
for _ in range(int(input())):
    n=int(input())
    score=[0,0]
    for i in range(n):
        a,b=map(int, input().split())
        if(a>9):
            a=sum(int(digit) for digit in str(a))
        if(b>9):
            b=sum(int(digit) for digit in str(b))
        #print(a,b)
        if a>b:
            score[0]+=1
        elif b>a:
            score[1]+=1
        else:
            score[0]+=1
            score[1]+=1
        #print(score)
    if(score[0]>score[1]):
        print(0,score[0])
    elif(score[1]>score[0]):
        print(1,score[1])
    else:
        print(2,score[0])