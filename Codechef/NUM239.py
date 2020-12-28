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
    l,r=inpmul()
    count=0
    for i in range(l,r+1):
        temp1=list(str(i))
        if temp1[len(temp1)-1]=="2" or temp1[len(temp1)-1]=="3" or temp1[len(temp1)-1]=="9":
            count+=1
    print(count)