from sys import stdin, stdout
import math,sys
from itertools import permutations, combinations
from collections import defaultdict,deque,OrderedDict,Counter
from os import path
from bisect import bisect_left 
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
    
####### ---- Start Your Program From Here ---- #######
for _ in range(inp()):
    n,t=minp()
    a=list(minp())
    for i in range(n):
        if a[i]>t/2:
            a[i]=0
        elif a[i]<t/2:
            a[i]=1
        else:
            a[i]=2
    equal=a.count(2)
    for i in range(n):
        if a[i]==2:
            if equal&1:
                a[i]=0
            else:
                a[i]=1
            equal-=1
    print(*a)