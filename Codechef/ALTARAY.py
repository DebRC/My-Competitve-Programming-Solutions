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
    o=[1]*n
    for i in range(n-2,-1,-1):
        if (a[i]<0 and a[i+1]>0) or (a[i]>0 and a[i+1]<0):
            o[i] += o[i+1]
    print(*o)