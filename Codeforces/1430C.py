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
    sys.stdin=open('input.txt','r');sys.stdout=open('output.txt','w')
    def inp():return (int(input()))
    def minp():return(map(int,input().split()))
else:
    #------------------PYPY FAst I/o--------------------------------#
    def inp():return (int(stdin.readline()))
    def minp():return(map(int,stdin.readline().split()))
    
####### ---- Start Your Program From Here ---- #####
for _ in range(inp()):
    n=inp()
    print(2)
    if n==2:
        print(1,2)
        continue
    a=[x for x in range(1,n+1)]
    if n&1:
        for i in range(n-1,0,-1):
            print(a[i],a[i-1])
            a[i-1]=math.ceil((a[i]+a[i-1])/2)
    else:
        print(a[n-1],a[n-3])
        a[n-3]=math.ceil((a[n-3]+a[n-1])/2)
        for i in range(n-2,0,-1):
            print(a[i],a[i-1])
            a[i-1]=math.ceil((a[i]+a[i-1])/2)