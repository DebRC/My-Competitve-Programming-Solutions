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
    a=[]
    for i in range(n):
        temp=intlist()
        a.append(temp)
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            a[i][j]=a[i][j]+max(a[i+1][j],a[i+1][j+1])
    print(a[0][0])