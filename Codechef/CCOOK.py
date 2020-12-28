# cook your dish here
for _ in range(int(input())):
    tot=0
    a=list(map(int,input().split()))
    tot=sum(a)
    if(tot==0):
        print("Beginner")
    elif(tot==1):
        print("Junior Developer")
    elif(tot==2):
        print("Middle Developer")
    elif(tot==3):
        print("Senior Developer")
    elif(tot==4):
        print("Hacker")
    elif(tot==5):
        print("Jeff Dean")