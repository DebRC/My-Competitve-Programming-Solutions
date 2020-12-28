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
    b=intlist()
    max_a=0
    max_b=0
    sum_a=0
    sum_b=0
    for i in range(n):
        if a[i]>max_a:
            max_a=a[i]
        if b[i]>max_b:
            max_b=b[i]
        sum_a+=a[i]
        sum_b+=b[i]
    if sum_a-max_a>sum_b-max_b:
        print("Bob")
    elif sum_a-max_a<sum_b-max_b:
        print("Alice")
    else:
        print("Draw")