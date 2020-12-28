# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if(x+y-z==0 or x-y+z==0 or -x+y+z==0 or x-y-z==0 or -x+y-z==0 or -x-y+z==0):
        print("yes")
    else:
        print("no")