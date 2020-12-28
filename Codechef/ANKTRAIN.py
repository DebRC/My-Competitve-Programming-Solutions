# cook your dish here
for _ in range(int(input())):
    n=int(input())
    b=n%8
    if(b==1):
        print(str(n+3)+"LB")
    elif(b==2):
        print(str(n+3)+"MB")
    elif(b==3):
        print(str(n+3)+"UB")
    elif(b==4):
        print(str(n-3)+"LB")
    elif(b==5):
        print(str(n-3)+"MB")
    elif(b==6):
        print(str(n-3)+"UB")
    elif(b==7):
        print(str(n+1)+"SU")
    elif(b==0):
        print(str(n-1)+"SL")
    