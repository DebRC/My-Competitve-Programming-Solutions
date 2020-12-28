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
    flag=0
    for i in range(n):
        if a[i]%2!=0:
            flag+=1
    if flag==n:
        print("YES")
    else:
        print("NO")