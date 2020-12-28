from sys import stdin, stdout
import math,sys
from itertools import permutations, combinations
from collections import defaultdict,deque,OrderedDict,Counter
from os import path
import bisect as bi
import heapq 
mod=10**9+7
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
    
####### ---- Start Your Program From Here ---- ######
def isPowerOfTwo (x):
    return not(x&(x-1))
for _ in range(inp()):
    n=inp()
    if n==1:
        print(1)
        continue
    if isPowerOfTwo(n) and n!=1:
        print(-1)
    else:
        a=[0]*n
        for i in range(n):
            a[i]=i+1
        if n==3:
            print(2,3,1)
            continue
        a[0],a[1],a[2],a[3],a[4]=2,3,1,5,4
        for i in range(5,n):
            if isPowerOfTwo(i+1):
                a[i],a[i+1]=a[i+1],a[i]
        for i in range(n):
            print(a[i],end=" ")
        print()