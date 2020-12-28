####### ---- Import Modules Here ---- #######
import sys
input = sys.stdin.readline
pstr = sys.stdout.write

####### ---- Input Functions ---- #######
def intinp():
    return(int(input()))
def intlist():
    return (list(map(int,input().split())))
def strlist():
    s = input()
    return (list(s[:len(s) - 1]))
def strinp():
    return (input())
def inpmul():
    return(map(int,input().split()))
    
####### ---- Start Your Program From Here ---- #######
for _ in range(intinp()):
    n=intinp()
    a=intlist()
    count=0
    for i in range(n):
        prod=1
        add=0
        for j in range(i,n):
            prod*=a[j]
            add+=a[j]
            if prod==add:
                count+=1
    print(count)