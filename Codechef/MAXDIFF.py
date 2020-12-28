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
    w=intlist()
    w.sort()
    w1=0
    w2=0
    if(k<=n-k):
        for i in range(k):
            w1+=w[i]
        for i in range(k,n):
            w2+=w[i]
    else:
        w.reverse()
        for i in range(k):
            w1+=w[i]
        for i in range(k,n):
            w2+=w[i]
    ans=abs(w1-w2)
    print(ans)