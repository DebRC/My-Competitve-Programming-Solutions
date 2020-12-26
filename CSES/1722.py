from sys import stdin, stdout
import math,sys
from itertools import permutations, combinations
from collections import defaultdict,deque,OrderedDict,Counter
from os import path
import bisect as bi
import heapq 
def yes():print('YES')
def no():print('NO')
if (path.exists('input.txt')): 
    #------------------Sublime--------------------------------------#
    sys.stdin=open('input.txt','r');sys.stdout=open('output.txt','w');
    def inp():return (int(input()))
    def minp():return(map(int,input().split()))
else:
    #------------------PYPY FAst I/o--------------------------------#
    def inp():return (int(stdin.readline()))
    def minp():return(map(int,stdin.readline().split()))
    
####### ---- Start Your Program From Here ---- #######
mod=10**9+7
def fibo(n):
    if n==-2:
        return 0
    if n==-1:
        return 1
    a=[[1,1],[1,0]]
    res=[[1,0],[0,1]]
    while(n):
        if n%2==1:
            res=matrixmulti(res,a)
            n-=1
        else:
            a=matrixmulti(a,a)
            n=n//2
    return (res[0][0]+res[0][1])%mod
def matrixmulti(m1,m2):
    mul=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                mul[i][j]=(mul[i][j]+(m1[i][k]*m2[k][j])%mod)%mod
    return mul
n=inp()
print(fibo(n-2))