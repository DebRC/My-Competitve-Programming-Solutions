# cook your dish here
for _ in range(int(input())):
    p=int(input())
    c=0
    while(p>0):
        if(p>=2048):
            p-=2048
        elif(p>=1024):
            p-=1024
        elif(p>=512):
            p-=512
        elif(p>=256):
            p-=256
        elif(p>=128):
            p-=128
        elif(p>=64):
            p-=64
        elif(p>=32):
            p-=32
        elif(p>=16):
            p-=16
        elif(p>=8):
            p-=8
        elif(p>=4):
            p-=4
        elif(p>=2):
            p-=2
        elif(p>=1):
            p-=1
        c+=1
    print(c)