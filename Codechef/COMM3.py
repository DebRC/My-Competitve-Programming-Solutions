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
    r=intinp()
    a=intlist()
    b=intlist()
    c=intlist()
    ab=(((a[0]-b[0])**2)+((a[1]-b[1])**2))**0.5
    bc=(((c[0]-b[0])**2)+((c[1]-b[1])**2))**0.5
    ca=(((a[0]-c[0])**2)+((a[1]-c[1])**2))**0.5
    if (ab>r and bc>r) or (ca>r and ab>r) or (bc>r and ca>r):
        print("no")
    else:
        print("yes")