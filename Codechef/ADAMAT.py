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
    
####### ---- Start Your Program From Here ---- #######
for _ in range(inp()):
    n=inp()
    a=[]
    for i in range(n):
        a.append(list(minp()))
    count=0
    new=[0]*n
    #horizontal mismatch
    for i in range(1,n+1):
        if i!=a[0][i-1]:
            new[i-1]=1
    #print(new)
    for i in range(n-1,0,-1):
        if new[i]==1:
            count+=1
            for i in range(i,0,-1):
                if new[i]==0:
                    new[i]=1
                else:
                    new[i]=0
            #print(new)
    print(count)