# cook your dish here
def hardness(n):
    if n>50:
        return 1
    else:
        return 0
def carbon(n):
    if n<0.7:
        return 1
    else:
        return 0
def tensile(n):
    if n>5600:
        return 1
    else:
        return 0
for _ in range(int(input())):
    h,c,t=list(map(float, input().split()))
    if(hardness(h)+carbon(c)+tensile(t)==3):
        print(10)
    elif(hardness(h)+carbon(c)==2):
        print(9)
    elif(carbon(c)+tensile(t)==2):
        print(8)
    elif(hardness(h)+tensile(t)==2):
        print(7)
    elif(hardness(h)+carbon(c)+tensile(t)==1):
        print(6)
    else:
        print(5)