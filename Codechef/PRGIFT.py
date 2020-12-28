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
    n,k=inpmul()
    a=intlist()
    count=0
    for i in range(n):
        if a[i]%2==0:
            count+=1
    if count==n and k==0:
        print("NO")
    elif count>=k:
        print("YES")
    else:
        print("NO")