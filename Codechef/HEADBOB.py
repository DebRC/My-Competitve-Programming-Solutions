# cook your dish here
for _ in range(int(input())):
    n=int(input())
    e=list(input())
    ey=e.count("Y")
    ei=e.count("I")
    if(ey>ei):
        print("NOT INDIAN")
    elif(ei>ey):
        print("INDIAN")
    else:
        print("NOT SURE")