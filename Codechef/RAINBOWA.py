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
k={1,2,3,4,5,6,7}
for _ in range(intinp()):
    n=intinp()
    a=intlist()
    if a[::-1]==a and set(a)==k :
        print("yes")
    else:
        print("no")
        