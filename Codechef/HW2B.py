# cook your dish here
import sys
input = sys.stdin.readline
############ ---- Input Functions ---- ############
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
n=intinp()
a=intlist()
total=2*(sum(a))//n
for i in range(n):
    if a[i]!=0:
        for j in range(i+1,n):
            if a[j]!=0 and a[i]+a[j]==total:
                print(i+1,j+1)
                a[i]=0
                a[j]=0